CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, Comission) VALUES
('S001', 'John Doe', 'New York', 0.10),
('S002', 'Jane Smith', 'Los Angeles', 0.12),
('S003', 'Mike Johnson', 'Chicago', 0.08),
('S004', 'Emily Davis', 'Houston', 0.15),
('S005', 'David Wilson', 'Phoenix', 0.09);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders(
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);

INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
('O001', 500.00, '2023-01-15', 'C001', 'S001'),
('O002', 750.00, '2023-02-20', 'C002', 'S002'),
('O003', 300.00, '2023-03-10', 'C003', 'S003'),
('O004', 1200.00, '2023-04-05', 'C004', 'S004'),
('O005', 450.00, '2023-02-20', 'C005', 'S005');

SELECT * FROM Orders;

SELECT name, Comission
FROM Salesman;

SELECT * FROM Salesman
WHERE city = 'New York';

SELECT * FROM orders
WHERE ord_date = '2023-02-20';