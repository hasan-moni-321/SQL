USING NULL

#1. SELECT name FROM teacher WHERE dept IS NULL
#2. SELECT teacher.name, dept.name FROM teacher JOIN dept ON (teacher.dept=dept.id)
#3. SELECT teacher.name,dept.name FROM teacher LEFT JOIN dept ON (teacher.dept=dept.id)
#4. SELECT teacher.name, dept.name FROM teacher RIGHT JOIN dept ON (teacher.dept=dept.id)
#5. SELECT name, COALESCE(mobile,'07986 444 2266') AS mobile FROM teacher
#6.
#7.
#8.
#9.
#10.