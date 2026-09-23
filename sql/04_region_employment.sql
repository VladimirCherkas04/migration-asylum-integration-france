SELECT
    r.region,
    r.main_city,
    COUNT(m.record_id) AS records,
    COUNT(*) FILTER (
        WHERE m.employment_status = 'Employed'
    ) AS employed,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE m.employment_status = 'Employed'
        ) / COUNT(*),
        2
    ) AS employment_rate_percent
FROM migration_records m
JOIN regions r
    ON m.region_id = r.region_id
GROUP BY
    r.region,
    r.main_city
ORDER BY employment_rate_percent DESC;