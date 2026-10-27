USE university_database;

CREATE TABLE department (
    dept_name VARCHAR(50) PRIMARY KEY,
    building VARCHAR(50),
    budget DECIMAL(12, 2)
);

INSERT INTO department VALUES ('CSE', 'Main Block', 100000.00);
INSERT INTO department VALUES ('ECE', 'VLSI Block', 95000.00);
INSERT INTO department VALUES ('IT', 'IT Block', 85000.00);
INSERT INTO department VALUES ('EEE', 'Electrical Block', 80000.00);

select * from department;