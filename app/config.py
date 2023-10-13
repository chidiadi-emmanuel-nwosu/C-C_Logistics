#!/usr/bin/python3
"""config file"""
import secrets
import os

class Config:
    SECRET_KEY = secrets.token_hex(16) #to avoid cookie modifications and CSRF (Cross-Site Request Forgery) attacks
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
