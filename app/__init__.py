#!/usr/bin/python3
"""init file"""
from flask import Flask
from app.routes import app_routes

app = Flask(__name__)
app.register_blueprint(app_routes)
