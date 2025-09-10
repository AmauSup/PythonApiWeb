# 🥛 Mammal Milk API  

A **RESTful API** built with **Flask** and **SQLAlchemy**, providing CRUD operations on mammal milk data stored in a **MySQL** database.  

This project was designed as a **demonstration of a simple Python web API**, focusing on clean architecture, database interaction, and maintainable code.  
*(The “mammal milk” theme started as a lighthearted joke among friends, but the implementation itself is fully professional.)*  

---

## 📌 Overview  

- **Framework**: Flask with Flask-CORS for cross-origin requests  
- **Database**: MySQL (via PHPMyAdmin)  
- **ORM**: SQLAlchemy  
- **Connector**: mysql-connector-python  
- **Language**: Python 3.x  

This project demonstrates:  
- Setting up a Python REST API with Flask  
- Using SQLAlchemy sessions with stored procedures  
- Following a modular service-based architecture  
- Writing clear documentation and logging for debugging  

---

## 🚀 Features  

- ✅ Retrieve all records (`GET`)  
- ✅ Insert new records via stored procedures (`POST`)  
- ✅ Update existing records (`PUT`)  
- ✅ Delete records (`DELETE`)  
- ✅ CORS support for frontend integration  
- ✅ Logging configured at DEBUG level for development  

---

## ⚡ Getting Started  

### ✅ Prerequisites  

- Python **3.10+**  
- MySQL installed locally (**with PHPMyAdmin** for easier management)  
- Database: `mammalmilkdb`  

---

### 🗄️ Database Setup  

```sql
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
```
📥 Installation
```
# Clone repository
git clone https://github.com/yourusername/mammal-milk-api.git
cd mammal-milk-api

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
▶️ Run the API
```
python main.py
```
The API will be available at:
👉 http://127.0.0.1:5000/
🌐 API Endpoints
🔹 Get all records
```
GET /get_milk
```
🔹 Create a record
```
POST /post_milk
```
Request body:
```
{
  "mammal": "Cow",
  "milk_quantity": 10.5
}
```
🔹 Update a record
```
PUT /put_milk/<milk_id>
```
Request body:
```
{
  "mammal": "Goat",
  "milk_quantity": 5.2
}
```
🔹 Delete a record
```
DELETE /del_milk/<milk_id>
```
📂 Project Structure
```
mammal-milk-api/
 ├── Database.py        # MySQL connection and session management
 ├── MilkService.py     # Business logic using stored procedures
 ├── FlaskApp.py        # Flask application and routes
 ├── main.py            # Application entry point
 ├── requirements.txt   # Python dependencies
 └── README.md          # Documentation
```
