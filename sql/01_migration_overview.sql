SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT country_of_origin) AS countries_of_origin,
    COUNT(DISTINCT region_id) AS regions_covered,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE employment_status = 'Employed')
        / COUNT(*),
        2
    ) AS employment_rate_percent
FROM migration_records;