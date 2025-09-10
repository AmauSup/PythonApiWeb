from sqlalchemy import create_engine  # Pour créer une connexion avec la base de données
from sqlalchemy.orm import sessionmaker  # Pour gérer les sessions avec la base de données

class Database:
    """
    Classe Database - Gère la connexion à une base de données MySQL
    et fournit des sessions pour interagir avec elle.
    """

    def __init__(self):
        """
        Initialise la connexion à la base de données en configurant l'engine SQLAlchemy
        et le gestionnaire de sessions.
        """
        # URL de connexion à la base de données MySQL
        # Format : "mysql+mysqlconnector://<utilisateur>:<mot_de_passe>@<hôte>:<port>/<nom_de_la_base>"
        self.db_url = "mysql+mysqlconnector://root:root@localhost:3306/mammalmilkdb"

        # Création de l'engine SQLAlchemy
        # echo=True affiche toutes les requêtes SQL pour faciliter le débogage
        self.engine = create_engine(self.db_url, echo=True)

        # Configuration d'une session factory avec SQLAlchemy
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """
        Crée et retourne une nouvelle session SQLAlchemy pour interagir avec la base.

        Returns:
            Session : Une instance de session SQLAlchemy.
        """
        return self.Session()
