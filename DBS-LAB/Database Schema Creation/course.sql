USE university_database;

CREATE TABLE course (
    course_id VARCHAR(20) PRIMARY KEY,
    title VARCHAR(100),
    dept_name VARCHAR(50),
    credits INT,
    FOREIGN KEY (dept_name) REFERENCES department(dept_name)
);

INSERT INTO course VALUES ('CSE-101', 'Data Structures', 'CSE', 4);
INSERT INTO course VALUES ('ECE-201', 'Digital Circuits', 'ECE', 3);
INSERT INTO course VALUES ('IT-301', 'Web Technologies', 'IT', 3);
INSERT INTO course VALUES ('EEE-102', 'Circuit Theory', 'EEE', 4);

INSERT INTO course VALUES ('ECE-202', 'Digital Circuits', 'ECE', 3);

-- Q4: Find the courses offered in both 'Fall' and 'Spring' semester ( sem - '2' & '5')

SELECT DISTINCT c.course_id, c.title
FROM course c
WHERE c.course_id IN (SELECT course_id FROM section WHERE semester = '2')
  AND c.course_id IN (SELECT course_id FROM section WHERE semester = '5');
  
-- Q6: Find the course id and titles of all courses taught by an instructor named 'Srinivasan'
SELECT DISTINCT c.course_id, c.title 
FROM course c
JOIN section s ON c.course_id = s.course_id
JOIN teaches t ON s.course_id = t.course_id AND s.sec_id = t.sec_id AND s.semester = t.semester AND s.year = t.year
JOIN instructor i ON t.ID = i.ID
WHERE i.name = 'Srinivasan';