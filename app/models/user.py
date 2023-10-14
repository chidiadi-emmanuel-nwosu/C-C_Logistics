#!/usr/bin/python3
"""user model"""
from flask_login import UserMixin
from app.models.base_model import BaseModel
from app import db


class User(BaseModel, db.Model, UserMixin):
    """user model"""
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    user_type = db.Column(db.String(30), default="user")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.user_type}')"
