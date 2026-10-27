USE university_database;

CREATE TABLE classroom (
    building VARCHAR(50),
    room_number VARCHAR(20),
    capacity INT,
    PRIMARY KEY (building, room_number)
);

INSERT INTO classroom VALUES ('Main Block', '312', 45);
INSERT INTO classroom VALUES ('VLSI Block', '211', 30);
INSERT INTO classroom VALUES ('IT Block', '120', 25);
INSERT INTO classroom VALUES ('Electrical Block', '408', 40);
INSERT INTO classroom VALUES ('VLSI Block', '212', 30);

select * from classroom;