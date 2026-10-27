USE university_database;

CREATE TABLE takes (
    s_id VARCHAR(20),
    course_id VARCHAR(20),
    sec_id VARCHAR(20),
    semester VARCHAR(20),
    year INT,
    grade VARCHAR(5),
    PRIMARY KEY (s_id, course_id, sec_id, semester, year),
    FOREIGN KEY (s_id) REFERENCES student(s_id),
    FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES section(course_id, sec_id, semester, year)
);

INSERT INTO takes VALUES ('160B01', 'CSE-101', '1', '5', 2023, 'A');
INSERT INTO takes VALUES ('200B02', 'IT-301', '1', '2', 2025, 'B+');
INSERT INTO takes VALUES ('260B03', 'ECE-202', '1', '2', 2025, 'O');

-- select * from takes;

-- Q2: Find the course id and grades of all courses taken by any student named 'Tanaka' ('Rahul')
SELECT t.course_id, t.grade 
FROM takes t 
JOIN student s ON t.s_id = s.s_id 
WHERE s.name = 'Rahul';