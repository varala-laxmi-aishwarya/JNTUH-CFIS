USE university_database;

CREATE TABLE prereq (
    course_id VARCHAR(20),
    prereq_id VARCHAR(20),
    PRIMARY KEY (course_id, prereq_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (prereq_id) REFERENCES course(course_id)
);

INSERT INTO prereq VALUES ('ECE-201', 'CSE-101');
INSERT INTO prereq VALUES ('IT-301', 'CSE-101');
INSERT INTO prereq VALUES ('EEE-102', 'ECE-201');