SELECT
    COUNT(*) AS total_cases,
    COUNT(DISTINCT country_of_citizenship) AS citizenship_countries,
    COUNT(DISTINCT region_id) AS regions_covered,
    COUNT(*) FILTER (
        WHERE decision = 'Accepted'
    ) AS accepted_cases,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE decision = 'Accepted'
        ) / COUNT(*),
        2
    ) AS acceptance_rate_percent
FROM asylum_cases;