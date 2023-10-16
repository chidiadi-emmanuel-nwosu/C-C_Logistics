#!/usr/bin/python3
"""create database models"""
from app import create_app, db
from app.models.user import User
from app.models.rider import Rider
from app.models.request import DeliveryRequest

app = create_app('development')
with app.app_context():
    # Create the database tables
    db.create_all()
