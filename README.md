Mammal Milk API

A lightweight RESTful API built with Flask and SQLAlchemy, enabling CRUD operations on mammal milk data stored in a MySQL database via PHPMyAdmin.

Table of Contents

Motivation

Features

Tech Stack

Getting Started

Prerequisites

Installation

Usage

API Endpoints

Project Structure

Contributing

License

Motivation

I built this API to demonstrate a clear, maintainable Flask application using SQLAlchemy with stored procedures. It serves as a clean example of combining backend APIs with relational data management — perfect for learning or showcasing best practices.

Features

Retrieve all milk records

Add new entries (via stored procedure)

Update existing data

Delete records

CORS support enabled for frontend integration

Full logging with debug mode for easy tracing

Tech Stack

Web Framework: Flask + flask-cors

ORM: SQLAlchemy

Database: MySQL (via PHPMyAdmin)

Connector: mysql-connector-python

Language: Python 3.x

Getting Started

Prerequisites:

Ensure MySQL is installed and accessible via PHPMyAdmin (e.g. on XAMPP/WAMP/MAMP).

Create a database named mammalmilkdb with the appropriate table and stored procedures.

SQL setup example:

CREATE TABLE mammal_milk (
id INT AUTO_INCREMENT PRIMARY KEY,
mammal VARCHAR(50) NOT NULL,
milk_quantity FLOAT NOT NULL
);

DELIMITER 
CREATEPROCEDUREAddMilkRecord(INpmammalVARCHAR(50),INpmilkquantityFLOAT)BEGININSERTINTOmammalmilk(mammal,milkquantity)VALUES(pmammal,pmilkquantity);END
CREATEPROCEDUREAddMilkRecord(INp
m
	​

ammalVARCHAR(50),INp
m
	​

ilk
q
	​

uantityFLOAT)BEGININSERTINTOmammal
m
	​

ilk(mammal,milk
q
	​

uantity)VALUES(p
m
	​

ammal,p
m
	​

ilk
q
	​

uantity);END

CREATE PROCEDURE UpdateMilkRecord(IN p_id INT, IN p_mammal VARCHAR(50), IN p_milk_quantity FLOAT)
BEGIN
UPDATE mammal_milk SET mammal = p_mammal, milk_quantity = p_milk_quantity WHERE id = p_id;
END$$

CREATE PROCEDURE DeleteMilkRecord(IN p_id INT)
BEGIN
DELETE FROM mammal_milk WHERE id = p_id;
END$$
DELIMITER ;

Installation:

Clone the repo
git clone https://github.com/yourusername/mammal-milk-api.git
