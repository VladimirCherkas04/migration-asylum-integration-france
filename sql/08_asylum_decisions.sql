SELECT
    decision,
    COUNT(*) AS cases,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS share_percent
FROM asylum_cases
GROUP BY decision
ORDER BY cases DESC;