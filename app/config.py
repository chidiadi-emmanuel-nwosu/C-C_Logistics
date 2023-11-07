#!/usr/bin/python3
"""config file"""
from os import getenv
import secrets
from itsdangerous import URLSafeTimedSerializer
from dotenv import load_dotenv


class Config:
    load_dotenv()
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///c_c-logistics.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = getenv('API_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'cclogisticsapp@gmail.com'
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = ('C&C logistics', 'cclogisticsapp@gmail.com')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

def configure():
    load_dotenv()

serialize_token = URLSafeTimedSerializer(Config.SECRET_KEY)
