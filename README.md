# Mammal Milk API

A lightweight RESTful API built with Flask and SQLAlchemy, enabling CRUD operations on mammal milk data stored in a MySQL database via PHPMyAdmin.

---

##  Table of Contents

- [Motivation](#motivation)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)

---

## Motivation

I built this API to demonstrate a clear, maintainable Flask application using SQLAlchemy with stored procedures. It serves as a clean example of combining backend APIs with relational data management — perfect for learning or showcasing best practices.

---

## Features

- Retrieve all milk records  
- Add new entries (via stored procedure)  
- Update existing data  
- Delete records  
- CORS support enabled for frontend integration  
- Full logging with debug mode for easy tracing  

---

## Tech Stack

| Component       | Technology                 |
|----------------|----------------------------|
| Web Framework   | Flask + flask-cors         |
| ORM             | SQLAlchemy                 |
| Database        | MySQL (via PHPMyAdmin)     |
| Connector       | mysql-connector-python     |
| Language        | Python 3.x                 |

---

## Getting Started

### Prerequisites

- Ensure MySQL is installed and accessible via PHPMyAdmin (e.g. on XAMPP/WAMP/MAMP).  
- Create a database named `mammalmilkdb` with the appropriate table and stored procedures (defined below).


CREATE TABLE mammal_milk (
  id INT AUTO_INCREMENT PRIMARY KEY,
  mammal VARCHAR(50) NOT NULL,
  milk_quantity FLOAT NOT NULL
);

DELIMITER $$
CREATE PROCEDURE AddMilkRecord(IN p_mammal VARCHAR(50), IN p_milk_quantity FLOAT)
BEGIN
  INSERT INTO mammal_milk(mammal, milk_quantity) VALUES (p_mammal, p_milk_quantity);
END$$
CREATE PROCEDURE UpdateMilkRecord(IN p_id INT, IN p_mammal VARCHAR(50), IN p_milk_quantity FLOAT)
BEGIN
  UPDATE mammal_milk SET mammal = p_mammal, milk_quantity = p_milk_quantity WHERE id = p_id;
END$$
CREATE PROCEDURE DeleteMilkRecord(IN p_id INT)
BEGIN
  DELETE FROM mammal_milk WHERE id = p_id;
END$$
DELIMITER ;

Installation

Clone the repo:

git clone https://github.com/yourusername/mammal-milk-api.git
cd mammal-milk-api

Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Start the API server:

python main.py

You should see:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

API Endpoints

    GET /get_milk
    Retrieve all milk records.

    POST /post_milk
    Create a new record.
    Request Body (JSON):

{
  "mammal": "Cow",
  "milk_quantity": 10.5
}

PUT /put_milk/<int:milk_id>
Update a record.
Request Body (JSON):

    {
      "mammal": "Goat",
      "milk_quantity": 5.2
    }

    DELETE /del_milk/<int:milk_id>
    Delete a specific record.

Project Structure

mammal-milk-api/
├── Database.py          # Handles MySQL connection & sessions
├── MilkService.py       # Business logic using stored procedures
├── FlaskApp.py          # Flask application and route definitions
├── main.py              # Launches the API server
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
