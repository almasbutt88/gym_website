DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS gym_class;
DROP TABLE IF EXISTS members;


CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);


CREATE TABLE gym_class(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    spaces INT,
    capacity INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    members_id INT REFERENCES members(id),
    classes_id INT REFERENCES gym_class(id)
);

INSERT INTO members (name, age) VALUES ('Joe', 40);
INSERT INTO members (name, age) VALUES ('Mary', 55);
INSERT INTO members (name, age) VALUES ('Lucy', 24);
INSERT INTO members (name, age) VALUES ('Chris', 17);
INSERT INTO members (name, age) VALUES ('Fraser', 40);
INSERT INTO members (name, age) VALUES ('Lee', 55);
INSERT INTO members (name, age) VALUES ('Sean', 24);
INSERT INTO members (name, age) VALUES ('Mike', 17);


INSERT INTO gym_class (name, spaces, capacity) VALUES ('Spin', 1, 5);
INSERT INTO gym_class (name, spaces, capacity) VALUES ('Zumba', 3, 5);
INSERT INTO gym_class (name, spaces, capacity) VALUES ('Body Combat', 4, 5);

INSERT INTO bookings (members_id, classes_id) VALUES (1, 3);