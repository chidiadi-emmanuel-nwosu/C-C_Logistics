#!/usr/bin/python3
"""config file"""
import secrets
from itsdangerous import URLSafeTimedSerializer
from dotenv import load_dotenv


class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///c_c-logistics.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
