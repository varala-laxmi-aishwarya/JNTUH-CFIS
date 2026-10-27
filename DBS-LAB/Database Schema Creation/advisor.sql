USE university_database;

CREATE TABLE advisor (
    s_id VARCHAR(20),
    i_id VARCHAR(20),
    PRIMARY KEY (s_id, i_id),
    FOREIGN KEY (s_id) REFERENCES student(s_id),
    FOREIGN KEY (i_id) REFERENCES instructor(ID)
);

INSERT INTO advisor VALUES ('160B01', '10101');
INSERT INTO advisor VALUES ('200B02', '20202');
INSERT INTO advisor VALUES ('260B03', '30102');