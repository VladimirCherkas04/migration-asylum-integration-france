SELECT
    program,
    COUNT(*) AS participants,
    COUNT(*) FILTER (
        WHERE completed = 'Yes'
    ) AS completed,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE completed = 'Yes'
        ) / COUNT(*),
        2
    ) AS completion_rate_percent,
    COUNT(*) FILTER (
        WHERE employment_outcome = 'Employed'
    ) AS employed_after_program,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE employment_outcome = 'Employed'
        ) / COUNT(*),
        2
    ) AS employment_outcome_rate_percent
FROM integration_support
GROUP BY program
ORDER BY employment_outcome_rate_percent DESC;