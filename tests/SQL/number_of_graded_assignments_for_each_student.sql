SELECT student_id, COUNT(*)
FROM assignments
WHERE state = 'GRADED'
GROUP BY student_id;
