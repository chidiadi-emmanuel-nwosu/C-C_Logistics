#!/usr/bin/python3
"""user model"""
from flask_login import UserMixin
from app.models.base_model import BaseModel
from app import db


class User(BaseModel, db.Model, UserMixin):
    """user model"""
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_email_verified = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    contact_address = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(30), default="user")

    def __repr__(self):
        return f"User ID: {self.id} Email: {self.email}"

    def to_dict(self, include_related=True):
        result = super().to_dict()

        if include_related and hasattr(self, 'deliveries'):
            result['deliveries'] = [delivery.to_dict(include_related=False)
                                    for delivery in self.deliveries]

        return result
