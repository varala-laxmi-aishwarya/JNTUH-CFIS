USE university_database;

CREATE TABLE instructor (
    ID VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50),
    dept_name VARCHAR(50),
    salary DECIMAL(10, 2),
    FOREIGN KEY (dept_name) REFERENCES department(dept_name)
);

INSERT INTO instructor VALUES ('10101', 'Srinivasan', 'CSE', 75000.00);
INSERT INTO instructor VALUES ('20202', 'Teja', 'ECE', 70000.00);
INSERT INTO instructor VALUES ('30102', 'Ravi Kumar', 'EEE', 90000.00);

-- select * from instructor;

-- Q3: Find the ID and name of instructors from outside Comp. Sci. who have taught a CSE course
-- Test data setup for this specific query
INSERT INTO instructor VALUES ('99001', 'Hari', 'CSE', 95000.00);
INSERT INTO teaches VALUES ('99001', 'CSE-101', '2', '2', 2025);

UPDATE instructor SET dept_name = 'ECE' WHERE ID = '99001';

-- Main Query
SELECT DISTINCT i.ID, i.name 
FROM instructor i
JOIN teaches t ON i.ID = t.ID
JOIN course c ON t.course_id = c.course_id
WHERE c.dept_name = 'CSE' AND i.dept_name != 'CSE';


-- Q5: Find the names of all the instructors from Comp. Sci. department
SELECT name 
FROM instructor 
WHERE dept_name = 'CSE';

-- Find names of instructors who have taught at least one course in Spring 2009 (sem - '2' , 2025)
SELECT DISTINCT i.name 
FROM instructor i
JOIN teaches t ON i.ID = t.ID
WHERE t.semester = '2' AND t.year = 2025;