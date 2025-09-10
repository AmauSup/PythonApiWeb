from sqlalchemy import text  # Pour écrire des requêtes SQL textuelles

class MilkService:
    """
    Service pour interagir avec la table 'mammal_milk' via SQL ou procédures stockées.
    """

    def __init__(self, db):
        """
        Initialise le service avec une instance de Database.

        Args:
            db (Database): Instance de la classe Database pour gérer les sessions.
        """
        self.db = db

    def get_all_milk(self):
        """
        Récupère tous les enregistrements de lait dans la base.

        Returns:
            list[dict]: Liste de dictionnaires représentant chaque enregistrement.
        """
        with self.db.get_session() as session:
            query = text("SELECT * FROM mammal_milk;")
            result = session.execute(query)
            rows = result.fetchall()
            columns = result.keys()

            # Convertit les résultats SQL en dictionnaires Python
            return [dict(zip(columns, row)) for row in rows]

    def add_milk_record(self, mammal, milk_quantity):
        """
        Ajoute un nouvel enregistrement dans la table 'mammal_milk'.

        Args:
            mammal (str): Nom de l'animal.
            milk_quantity (float): Quantité de lait.
        """
        with self.db.get_session() as session:
            query = text("CALL AddMilkRecord(:mammal, :milk_quantity);")
            session.execute(query, {"mammal": mammal, "milk_quantity": milk_quantity})
            session.commit()  # Enregistre les modifications dans la base

    def update_milk_record(self, milk_id, mammal, milk_quantity):
        """
        Met à jour un enregistrement existant dans la table.

        Args:
            milk_id (int): ID de l'enregistrement.
            mammal (str): Nouveau nom de l'animal.
            milk_quantity (float): Nouvelle quantité de lait.
        """
        with self.db.get_session() as session:
            query = text("CALL UpdateMilkRecord(:milk_id, :mammal, :milk_quantity);")
            session.execute(query, {"milk_id": milk_id, "mammal": mammal, "milk_quantity": milk_quantity})
            session.commit()

    def delete_milk_record(self, milk_id):
        """
        Supprime un enregistrement de la table 'mammal_milk'.

        Args:
            milk_id (int): ID de l'enregistrement à supprimer.
        """
        with self.db.get_session() as session:
            query = text("CALL DeleteMilkRecord(:milk_id);")
            session.execute(query, {"milk_id": milk_id})
            session.commit()
