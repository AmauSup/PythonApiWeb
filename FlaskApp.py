from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

from Database import Database
from MilkService import MilkService

class FlaskApp:
    """
    Application web Flask pour exposer l'API CRUD de la table 'mammal_milk'.
    """

    def __init__(self):
        # Création de l'application Flask
        self.app = Flask(__name__)

        # Activation de CORS pour toutes les origines
        CORS(self.app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

        # Instances Database et MilkService
        self.db = Database()
        self.service = MilkService(self.db)

        # Définition des routes
        self.setup_routes()

    def setup_routes(self):
        """
        Définit les endpoints de l'API.
        """

        @self.app.route('/get_milk', methods=['GET'])
        def get_all_milk():
            logging.debug("GET /get_milk")
            milk_records = self.service.get_all_milk()
            return jsonify(milk_records)

        @self.app.route('/post_milk', methods=['POST'])
        def create_milk_record():
            logging.debug("POST /post_milk")
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid JSON or Content-Type"}), 400
            self.service.add_milk_record(data['mammal'], data['milk_quantity'])
            return jsonify({"message": "Record created successfully"}), 201

        @self.app.route('/put_milk/<int:milk_id>', methods=['PUT'])
        def update_milk_record(milk_id):
            logging.debug(f"PUT /put_milk/{milk_id}")
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid JSON or Content-Type"}), 400
            self.service.update_milk_record(milk_id, data['mammal'], data['milk_quantity'])
            return jsonify({"message": "Record updated successfully"})

        @self.app.route('/del_milk/<int:milk_id>', methods=['DELETE'])
        def delete_milk_record(milk_id):
            logging.debug(f"DELETE /del_milk/{milk_id}")
            self.service.delete_milk_record(milk_id)
            return jsonify({"message": "Record deleted successfully"})

    def run(self):
        """
        Démarre le serveur Flask en local sur le port 5000.
        """
        print("Démarrage du serveur Flask...")
        self.app.run(host='127.0.0.1', port=5000, debug=True)
