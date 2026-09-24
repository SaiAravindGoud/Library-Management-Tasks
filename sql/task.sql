CREATE DATABASE library1_db;
USE library1_db;
SELECT DATABASE();
CREATE TABLE Books (
    Book_ID INT PRIMARY KEY AUTO_INCREMENT,
    Book_Name VARCHAR(100) NOT NULL,
    Author_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10,2),
    Available_Copies INT DEFAULT 0
);
SHOW TABLES;
DESCRIBE Books;
CREATE TABLE Members (
    Member_ID INT PRIMARY KEY AUTO_INCREMENT,
    Member_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15)
);
SHOW TABLES;
DESCRIBE Members;
CREATE TABLE Borrow_Records (
    Borrow_ID INT PRIMARY KEY AUTO_INCREMENT,
    Book_ID INT NOT NULL,
    Member_ID INT NOT NULL,
    Borrow_Date DATE NOT NULL,
    Return_Date DATE,
    
    FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID),
    FOREIGN KEY (Member_ID) REFERENCES Members(Member_ID)
);
SHOW TABLES;
DESCRIBE Borrow_Records;
INSERT INTO Books
(Book_Name, Author_Name, Category, Price, Available_Copies)
VALUES
('The Alchemist', 'Paulo Coelho', 'Fiction', 350.00, 5),
('Wings of Fire', 'A.P.J. Abdul Kalam', 'Biography', 300.00, 8),
('Clean Code', 'Robert C. Martin', 'Programming', 650.00, 4),
('Atomic Habits', 'James Clear', 'Self Help', 500.00, 6),
('Harry Potter', 'J.K. Rowling', 'Fantasy', 450.00, 3);
SELECT * FROM Books;
INSERT INTO Members
(Member_Name, Email, Phone)
VALUES
('Rahul Sharma', 'rahul@gmail.com', '9876543210'),
('Priya Reddy', 'priya@gmail.com', '9876543211'),
('Arun Kumar', 'arun@gmail.com', '9876543212'),
('Sneha Rao', 'sneha@gmail.com', '9876543213'),
('Vikram Singh', 'vikram@gmail.com', '9876543214');
SELECT * FROM Members;
INSERT INTO Borrow_Records
(Book_ID, Member_ID, Borrow_Date, Return_Date)
VALUES
(1, 1, '2026-09-01', '2026-09-10'),
(2, 2, '2026-09-03', '2026-09-12'),
(3, 3, '2026-09-05', NULL),
(4, 4, '2026-09-07', '2026-09-15'),
(5, 5, '2026-09-10', NULL);
SELECT * FROM Borrow_Records;
SELECT
    Borrow_ID,
    Book_ID,
    Member_ID,
    Borrow_Date,
    Return_Date
FROM Borrow_Records;
INSERT INTO Books
(Book_Name, Author_Name, Category, Price, Available_Copies)
VALUES
('Python Crash Course', 'Eric Matthes', 'Programming', 700.00, 7);
SELECT * FROM Books;
SELECT *
FROM Books
WHERE Book_ID = 3;
UPDATE Books
SET Price = 750.00
WHERE Book_ID = 3;
DELETE FROM Books
WHERE Book_ID = 6;
SELECT * FROM Books;
SELECT
    br.Borrow_ID,
    b.Book_Name,
    m.Member_Name,
    br.Borrow_Date,
    br.Return_Date
FROM Borrow_Records br
JOIN Books b
    ON br.Book_ID = b.Book_ID
JOIN Members m
    ON br.Member_ID = m.Member_ID;
    SELECT
    Category,
    COUNT(*) AS Total_Books
FROM Books
GROUP BY Category;
SELECT
    Book_ID,
    Book_Name,
    Category,
    Price
FROM Books
ORDER BY Price DESC;
SELECT
    COUNT(*) AS Total_Books,
    SUM(Price) AS Total_Book_Value,
    AVG(Price) AS Average_Price,
    MAX(Price) AS Highest_Price,
    MIN(Price) AS Lowest_Price
FROM Books;
CREATE VIEW Borrowed_Book_Report AS
SELECT
    br.Borrow_ID,
    b.Book_Name,
    b.Author_Name,
    m.Member_Name,
    m.Email,
    br.Borrow_Date,
    br.Return_Date
FROM Borrow_Records br
JOIN Books b
    ON br.Book_ID = b.Book_ID
JOIN Members m
    ON br.Member_ID = m.Member_ID;
  SELECT * FROM Borrowed_Book_Report;
  SHOW FULL TABLES
WHERE TABLE_TYPE = 'VIEW';