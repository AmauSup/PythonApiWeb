# 🥛 Mammal Milk API

A simple Python REST API for managing mammal milk records, backed by a MySQL database (phpMyAdmin).  
This project was created as a fun experiment to practice Python, Flask, and SQL.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Database**: MySQL (phpMyAdmin)  
- **Testing**: Postman / cURL  

---

## 📦 Installation

1. Clone the repository:

git clone https://github.com/AmauSup/PythonApiWeb.git
cd mammal-milk-api

    Install dependencies (preferably in a virtual environment):

pip install -r requirements.txt

    Set up your MySQL database (phpMyAdmin):

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

    Launch the API:

python main.py

📬 Example Requests

Get all milk records:

curl http://127.0.0.1:5000/get_milk

Add a new milk record:

curl -X POST http://127.0.0.1:5000/post_milk \
-H "Content-Type: application/json" \
-d '{"mammal": "Cow", "milk_quantity": 10.5}'

Update a milk record (ID = 1):

curl -X PUT http://127.0.0.1:5000/put_milk/1 \
-H "Content-Type: application/json" \
-d '{"mammal": "Cow", "milk_quantity": 12.0}'

Delete a milk record (ID = 1):

curl -X DELETE http://127.0.0.1:5000/del_milk/1

    You can also test all endpoints with Postman.
