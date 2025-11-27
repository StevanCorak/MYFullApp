from flask import Flask
from .ui.routes import ui_bp
import os

def create_app():
    """
    Stvara i konfigurira Flask aplikaciju.
    """
    app = Flask(__name__, instance_relative_config=True)
    
    # Postavljanje jednostavne konfiguracije. 
    # U stvarnom sustavu, ovo bi bilo kompleksnije.
    app.config.from_mapping(
        SECRET_KEY='dev_secret_key_for_checkpoint1',
    )

    # Stvaranje foldera za instance (nije striktno potrebno, ali je dobra praksa)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Registracija Blueprinta (skupine ruta) za korisničko sučelje
    app.register_blueprint(ui_bp)

    return app