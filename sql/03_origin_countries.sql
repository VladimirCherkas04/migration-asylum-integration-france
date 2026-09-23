SELECT
    country_of_origin,
    COUNT(*) AS records,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS share_percent
FROM migration_records
GROUP BY country_of_origin
ORDER BY records DESC;