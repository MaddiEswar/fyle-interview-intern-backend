SELECT teacher_id, COUNT(*)
FROM assignments
WHERE grade = 'A'
GROUP BY teacher_id
ORDER BY COUNT(*) DESC
LIMIT 1;
