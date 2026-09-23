WITH regional_stats AS (
    SELECT
        r.region,
        r.main_city,
        COUNT(m.record_id) AS total_records,
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
),

overall_stats AS (
    SELECT
        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE employment_status = 'Employed'
            ) / COUNT(*),
            2
        ) AS overall_employment_rate
    FROM migration_records
)

SELECT
    rs.region,
    rs.main_city,
    rs.total_records,
    rs.employment_rate_percent,
    os.overall_employment_rate,
    ROUND(
        rs.employment_rate_percent - os.overall_employment_rate,
        2
    ) AS difference_from_overall,
    RANK() OVER (
        ORDER BY rs.employment_rate_percent DESC
    ) AS regional_rank
FROM regional_stats rs
CROSS JOIN overall_stats os
ORDER BY regional_rank;