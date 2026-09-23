SELECT
    age_group,
    COUNT(*) AS records,
    COUNT(*) FILTER (
        WHERE employment_status = 'Employed'
    ) AS employed,
    COUNT(*) FILTER (
        WHERE employment_status = 'Unemployed'
    ) AS unemployed,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE employment_status = 'Employed'
        ) / COUNT(*),
        2
    ) AS employment_rate_percent
FROM migration_records
GROUP BY age_group
ORDER BY employment_rate_percent DESC;