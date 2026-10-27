USE university_database;

CREATE TABLE time_slot (
    time_slot_id VARCHAR(20) PRIMARY KEY,
    day VARCHAR(10),
    start_time TIME,
    end_time TIME
);

INSERT INTO time_slot VALUES ('T1', 'M', '09:00:00', '10:00:00');
INSERT INTO time_slot VALUES ('T2', 'W', '11:00:00', '12:00:00');