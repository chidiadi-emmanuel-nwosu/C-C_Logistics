#!/usr/bin/python3
"""models"""
import uuid
from datetime import datetime
from app import db


class BaseModel():
    """base model super class"""
    id = db.Column(db.String(60), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


    def __init__(self, *args, **kwargs):
        """initialises the class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f"))
                if key != '__class__':
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()


    def __str__(self):
        """return on print"""
        return f"({self.__class__.__name__}) ({self.id}) {self.to_dict()}"


    def to_dict(self):
        """returns a dictionary of class attributes and values"""
        new = self.__dict__.copy()
        if "created_at" in new:
            new['created_at'] = new['created_at'].strftime("%Y-%m-%d %H:%M:%S.%f")
        if "updated_at" in new:
            new['updated_at'] = new['updated_at'].strftime("%Y-%m-%d %H:%M:%S.%f")
        if "date_of_birth" in new:
            new['date_of_birth'] = new['date_of_birth'].strftime("%Y-%m-%d %H:%M:%S.%f")
        if "password" in new:
            del new['password']
        if "_sa_instance_state" in new:
            del new['_sa_instance_state']

        return new
