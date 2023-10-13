#!/usr/bin/python3
"""config file"""
import secrets
import os

class Config:
    pass
    # SECRET_KEY = secrets.token_hex(16)
    # SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
