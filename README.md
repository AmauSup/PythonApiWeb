# 🥛 API Milk des Mammifères

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.2-blue.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://www.mysql.com/)

Une **API RESTful** construite avec **Flask** et **SQLAlchemy**, fournissant des opérations CRUD sur les données de lait des mammifères stockées dans une base de données **MySQL**.

Ce projet a été conçu comme une **démonstration d'une API web Python simple**, avec un focus sur une architecture propre, l’interaction avec la base de données et un code maintenable.  
*(Le thème “lait des mammifères” a commencé comme une plaisanterie entre amis, mais l’implémentation est entièrement professionnelle.)*

---

## 📌 Vue d'ensemble

- **Framework** : Flask avec Flask-CORS pour les requêtes cross-origin  
- **Base de données** : MySQL (via PHPMyAdmin)  
- **ORM** : SQLAlchemy  
- **Connecteur** : mysql-connector-python  
- **Langage** : Python 3.x  

Ce projet montre :  
- Comment configurer une API REST Python avec Flask  
- L’utilisation des sessions SQLAlchemy avec des procédures stockées  
- Le respect d’une architecture modulaire basée sur des services  
- La rédaction d’une documentation claire et d’un logging pour le débogage

---

## 🚀 Fonctionnalités

- ✅ Récupérer tous les enregistrements (`GET`)  
- ✅ Insérer de nouveaux enregistrements via des procédures stockées (`POST`)  
- ✅ Mettre à jour des enregistrements existants (`PUT`)  
- ✅ Supprimer des enregistrements (`DELETE`)  
- ✅ Support CORS pour l’intégration frontend  
- ✅ Logging configuré en niveau DEBUG pour le développement

---

## ⚡ Démarrage

### ✅ Prérequis

- Python **3.10+**  
- MySQL installé localement (**avec PHPMyAdmin** pour une gestion plus facile)  
- Base de données : `mammalmilkdb`

---

### 🗄️ Configuration de la base de données

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

```bash
# Cloner le dépôt
git clone https://github.com/yourusername/mammal-milk-api.git
cd mammal-milk-api

# Créer et activer un environnement virtuel
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

```
▶️ Lancer l’API
```
python main.py
```
L’API sera disponible à :
👉 http://127.0.0.1:5000/
🌐 Endpoints de l’API
🔹 Récupérer tous les enregistrements
```
GET /get_milk
```
🔹 Créer un enregistrement
```
POST /post_milk
```
Corps de la requête :
```
{
  "mammal": "Cow",
  "milk_quantity": 10.5
}
```
🔹 Mettre à jour un enregistrement
```
PUT /put_milk/<milk_id>
```
Corps de la requête :
```
{
  "mammal": "Goat",
  "milk_quantity": 5.2
}
```
🔹 Supprimer un enregistrement
```
DELETE /del_milk/<milk_id>
```
📂 Structure du projet
```
mammal-milk-api/
 ├── Database.py        # MySQL connection and session management
 ├── MilkService.py     # Business logic using stored procedures
 ├── FlaskApp.py        # Flask application and routes
 ├── main.py            # Application entry point
 ├── requirements.txt   # Python dependencies
 └── README.md          # Documentation
```
✅ Conclusion

Ce projet illustre comment concevoir et implémenter une API REST Python simple mais robuste, avec une architecture propre, une intégration à la base de données et une documentation claire.

Même si le thème du lait des mammifères est ludique, l’objectif était de mettre en avant des pratiques professionnelles : code modulaire, opérations structurées sur la base de données et design maintenable.

Il peut servir à la fois de ressource pédagogique pour les débutants et de base solide pour des projets API plus complexes.
