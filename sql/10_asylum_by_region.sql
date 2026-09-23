SELECT
    r.region,
    r.main_city,
    COUNT(a.case_id) AS total_cases,
    COUNT(*) FILTER (
        WHERE a.decision = 'Accepted'
    ) AS accepted_cases,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE a.decision = 'Accepted'
        ) / COUNT(*),
        2
    ) AS acceptance_rate_percent
FROM asylum_cases a
JOIN regions r
    ON a.region_id = r.region_id
GROUP BY
    r.region,
    r.main_city
HAVING COUNT(a.case_id) > 100
ORDER BY acceptance_rate_percent DESC;