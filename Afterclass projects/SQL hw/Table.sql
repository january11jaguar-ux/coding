
CREATE TABLE fruits (
    name TEXT PRIMARY KEY,
    color TEXT,
    price INTERGER
);

INSERT INTO fruits(name, color, price) VALUES
('Apple', 'Red', 10),
('Banana', 'Yellow', 20),
('Grapes', 'Green', 15),
('Orange', 'Orange', 10),
('Mango', 'Yellow', 25);
SELECT * FROM fruits;

SELECT color, price 
FROM fruits;

SELECT * FROM fruits
WHERE color = 'Yellow';

SELECT * FROM fruits 
WHERE price = '10';