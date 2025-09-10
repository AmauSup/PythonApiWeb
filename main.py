import logging
from FlaskApp import FlaskApp

# Configuration du logging pour le débogage
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    # Création et lancement de l'application Flask
    app = FlaskApp()
    app.run()
