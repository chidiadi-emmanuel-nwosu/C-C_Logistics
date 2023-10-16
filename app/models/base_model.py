#!/usr/bin/python3
"""models"""
import uuid
from datetime import datetime
from app import db


class BaseModel():
    """base model super class"""
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.String(60), nullable=False)
    updated_at = db.Column(db.String(60), nullable=False)


    def __init__(self, *args, **kwargs):
        """initialises the class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                if key != '__class__':
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.utcnow()


    def __str__(self):
        """return on print"""
        return f"({self.__class__.__name__}) ({self.id}) {self.to_dict()}"


    def to_dict(self):
        """returns a dictionary of class attributes and values"""
        new = self.__dict__.copy()
        if "created_at" in new:
            new['created_at'] = self.created_at.isoformat()
        if "updated_at" in new:
            new['updated_at'] = self.updated_at.isoformat()
        if "password" in new:
            del new['password']
        if "_sa_instance_state" in new:
            del new['_sa_instance_state']

        return new
