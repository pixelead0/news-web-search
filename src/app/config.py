import os


class Config:
    """Config flask"""
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get("SECRET_KEY", "placeholder-secret-key")

    DB_PSW = os.environ.get('DB_PSW')
    DB_USER = os.environ.get('DB_USER')
    DB_NAME = os.environ.get('DB_NAME')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PSW}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
