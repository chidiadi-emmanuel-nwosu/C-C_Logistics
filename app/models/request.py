#!/usr/bin/python3
"""order model"""
from datetime import datetime
from app.models.base_model import BaseModel
from app import db


class DeliveryRequest(BaseModel, db.Model):
    """order class for order details"""
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rider_id = db.Column(db.Integer, db.ForeignKey('rider.id'))
    pickup_address = db.Column(db.String(200), nullable=False)
    pickup_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    item_description = db.Column(db.String(50), nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    delivery_instruction = db.Column(db.String(400), nullable=True)
    order_status = db.Column(db.String(20), nullable=False, default="pending")
    user = db.relationship('User', foreign_keys=[user_id], backref='orders')
    rider = db.relationship('Rider', foreign_keys=[rider_id], backref='orders')

    def __repr__(self):
        return (f"Request by: {self.user}, "
                f"accepted by: {self.rider}, "
                f"order status: {self.Order_status}")
