from flask import Flask
from .ui.routes import ui_bp
import os

def create_app():
    """
    Stvara i konfigurira Flask aplikaciju.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev_secret_key_for_checkpoint1',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(ui_bp)

    return app