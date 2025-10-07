"""
Inicialización de la aplicación Flask.

Este módulo:
- Crea la instancia de Flask.
- Configura la app según el entorno.
- Inicializa extensiones como SQLAlchemy.
- Crea las tablas de la base de datos y carga datos iniciales.
- Registra blueprints de rutas y manejo de errores.
"""

from flask import Flask
from .extensions import db
from .config import config
from .errors import errors
from app.models import *  # Importa todos los modelos para que SQLAlchemy los reconozca
from app.seeds import seed_products  # Función para insertar datos iniciales
from app.routes.products import bp  # Blueprint de productos


def create_app():
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(
        config["development"] # Cambiar a 'development' o 'production' según sea necesario
    )  
    # Inicializar extensiones
    db.init_app(app)

    # Crear tablas y cargar datos de ejemplo
    with app.app_context():
        db.create_all()
        seed_products()

    # Registrar rutas y manejadores de errores
    app.register_blueprint(bp)
    app.register_blueprint(errors)

    return app
