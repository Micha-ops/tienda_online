import os
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env al entorno de Python
load_dotenv()


class Config:
    # Datos de conexión a PostgreSQL, tomados del .env
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres123")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "tienda_online")

    # SQLAlchemy necesita esta URI con el formato:
    # postgresql://usuario:contraseña@host:puerto/nombre_basedatos
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Desactiva una función de SQLAlchemy que no usaremos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para sesiones de Flask (login, mensajes, etc.)
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-de-desarrollo-temporal")
