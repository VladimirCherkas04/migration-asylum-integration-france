SELECT
    EXTRACT(YEAR FROM date)::INTEGER AS year,
    COUNT(*) AS migration_records,
    COUNT(*) FILTER (WHERE employment_status = 'Employed') AS employed_records,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE employment_status = 'Employed')
        / COUNT(*),
        2
    ) AS employment_rate_percent
FROM migration_records
GROUP BY EXTRACT(YEAR FROM date)
ORDER BY year;