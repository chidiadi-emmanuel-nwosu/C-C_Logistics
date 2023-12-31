#!/usr/bin/python3
"""order model"""
from datetime import datetime
from app.models.base_model import BaseModel
from app import db


class DeliveryRequest(BaseModel, db.Model):
    """order class for order details"""
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('delivery_agent.id'))
    pickup_address = db.Column(db.String(200), nullable=False)
    pickup_time = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    item_description = db.Column(db.String(50), nullable=False)
    contact_person = db.Column(db.String(50), nullable=False)
    contact_phone_number = db.Column(db.String(15), nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=False,
                              default=datetime.utcnow())
    delivery_instruction = db.Column(db.String(400))
    estimated_distance = db.Column(db.String(15), nullable=False)
    estimated_duration = db.Column(db.String(15), nullable=False)
    delivery_cost = db.Column(db.String(20), nullable=False)
    order_status = db.Column(db.String(20), nullable=False, default="pending")
    user = db.relationship('User', foreign_keys=[user_id],
                           backref='deliveries')
    agent = db.relationship('DeliveryAgent',
                            foreign_keys=[agent_id], backref='deliveries')

    def to_dict(self, include_related=True):
        result = super().to_dict()

        if include_related:
            result['user'] = (self.user.to_dict(include_related=False)
                              if self.user else None)
            result['agent'] = (self.agent.to_dict(include_related=False)
                               if self.agent else None)

        return result
    def __repr__(self):
        return f'User_id: {self.user_id}, {self.agent_id}'