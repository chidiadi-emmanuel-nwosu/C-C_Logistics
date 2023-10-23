#!/usr/bin/python3
"""user model"""
from flask_login import UserMixin
from app.models.base_model import BaseModel
from app import db


class DeliveryAgent(BaseModel, db.Model, UserMixin):
    """rider class for agent datas"""
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_email_verified = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    contact_address = db.Column(db.String(200), nullable=False)
    drivers_license_number = db.Column(db.String(10), nullable=False, unique=True)
    license_expiration_date = db.Column(db.Date, nullable=False)
    license_image_file = db.Column(db.LargeBinary, nullable=False)
