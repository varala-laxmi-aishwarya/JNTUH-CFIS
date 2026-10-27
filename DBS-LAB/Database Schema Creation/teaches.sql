USE university_database;

CREATE TABLE teaches (
    ID VARCHAR(20),
    course_id VARCHAR(20),
    sec_id VARCHAR(20),
    semester VARCHAR(20),
    year INT,
    PRIMARY KEY (ID, course_id, sec_id, semester, year),
    FOREIGN KEY (ID) REFERENCES instructor(ID),
    FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES section(course_id, sec_id, semester, year)
);

INSERT INTO teaches VALUES ('10101', 'CSE-101', '1', '5', 2023);
INSERT INTO teaches VALUES ('20202', 'ECE-201', '1', '4', 2024);
INSERT INTO teaches VALUES ('20202', 'ECE-202', '1', '2', 2025);
-- INSERT INTO teaches VALUES ('99001', 'CSE-101', '2', '2', 2025);

select * from teaches;

