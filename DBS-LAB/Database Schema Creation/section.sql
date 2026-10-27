USE university_database;

CREATE TABLE section (
    course_id VARCHAR(20),
    sec_id VARCHAR(20),
    semester VARCHAR(20),
    year INT,
    building VARCHAR(50),
    room_number VARCHAR(20),
    time_slot_id VARCHAR(20),
    PRIMARY KEY (course_id, sec_id, semester, year),
    FOREIGN KEY (course_id) REFERENCES course(course_id),
    FOREIGN KEY (building, room_number) REFERENCES classroom(building, room_number),
    FOREIGN KEY (time_slot_id) REFERENCES time_slot(time_slot_id)
);

INSERT INTO section VALUES ('CSE-101', '1', '5', 2023, 'Main Block', '312', 'T1');
INSERT INTO section VALUES ('CSE-101', '2', '2', 2025, 'Main Block', '312', 'T2');
INSERT INTO section VALUES ('ECE-201', '1', '4', 2024, 'VLSI Block', '211', 'T1');
INSERT INTO section VALUES ('ECE-202', '1', '2', 2025, 'VLSI Block', '212', 'T2');
INSERT INTO section VALUES ('IT-301', '1', '2', 2025, 'IT Block', '120', 'T1');


select * from section;