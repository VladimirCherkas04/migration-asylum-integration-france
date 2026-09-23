SELECT
    country_of_citizenship,
    COUNT(*) AS cases,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS share_percent
FROM asylum_cases
GROUP BY country_of_citizenship
ORDER BY cases DESC;