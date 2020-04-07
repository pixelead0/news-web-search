import os


class Config:
    """Config flask"""
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get("SECRET_KEY", "placeholder-secret-key")

    DB_PSW = os.environ.get('DB_PSW', 'dev_psw')
    DB_USER = os.environ.get('DB_USER', 'dev_user')
    DB_NAME = os.environ.get('DB_NAME', 'dev_db')
    DB_HOST = os.environ.get('DB_HOST', 'postgres')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PSW}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
