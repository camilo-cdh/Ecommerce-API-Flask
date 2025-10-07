import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()


class BaseConfig:

    # Configuración base compartida
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """
    Configuración para desarrollo y pruebas.
    Usa SQLite para pruebas rapidas.
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{os.getenv('DATABASE_PATH')}{os.getenv('DATABASE_NAME')}"
    )


class ProductionConfig(BaseConfig):
    """
    Configuración  para producción.
    Usa MySQL y toma los datos de conexión desde variables de entorno.
    """

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )


# Diccionario para seleccionar configuración
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
