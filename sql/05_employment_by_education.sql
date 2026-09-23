SELECT
    education_level,
    COUNT(*) AS records,
    COUNT(*) FILTER (
        WHERE employment_status = 'Employed'
    ) AS employed,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE employment_status = 'Employed'
        ) / COUNT(*),
        2
    ) AS employment_rate_percent
FROM migration_records
GROUP BY education_level
ORDER BY employment_rate_percent DESC;