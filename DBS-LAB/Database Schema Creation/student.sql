USE university_database;

CREATE TABLE student (
    s_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(50),
    dept_name VARCHAR(50),
    tot_cred INT,
    FOREIGN KEY (dept_name) REFERENCES department(dept_name)
);

INSERT INTO student VALUES ('160B01', 'Rahul', 'CSE', 105);
INSERT INTO student VALUES ('200B02', 'Priyanka', 'IT', 85);
INSERT INTO student VALUES ('260B03', 'Shyam', 'CSE', 115);

UPDATE student SET dept_name = 'ECE' WHERE s_id = '260B03';

-- select * from student;

-- Q1: Find the names of all the students whose total credits are greater than 100
SELECT name 
FROM student 
WHERE tot_cred > 100;