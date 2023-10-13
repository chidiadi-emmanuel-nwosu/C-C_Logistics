from datetime import datetime, date
from app import db, login_manager #login_manager manages our login sessions
from flask_login import UserMixin #to simplify user authentication in your Flask application

@login_manager.user_loader #this is a decorator convenction
def load_user(user_id): #this is a function that will return the id of a user to us
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): #By inheriting from UserMixin, your custom user model gains several 
    #attributes and methods, including is_authenticated, is_active, is_anonymous, and get_id, which are essential for user authentication

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False)
    user_type = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.user_type}')"

class Rider(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(20), nullable=False)
    Last_name = db.Column(db.String(30), nullable=False)
    Date_of_birth = db.Column(db.Date, nullable=False)
    marital_status = db.Column(db.String(20), nullable=True)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    Phone_number = db.Column(db.String(11), nullable=False)
    Contact_address = db.Column(db.String(80), nullable=False)
    Drivers_license = db.Column(db.String(10), nullable=False, unique=True)
    Expiration_date = db.Column(db.Date, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')

    def __repr__(self):
        return f"Rider('{self.First_name}', '{self.Last_name}', '{self.image_file}')"

class Order(db.Model):
    Order_id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Rider_id = db.Column(db.Integer, db.ForeignKey('rider.id'))
    Pickup_address = db.Column(db.String(200), nullable=False)
    Pickup_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Item_description = db.Column(db.String(50), nullable=False)
    Delivery_address = db.Column(db.String(200), nullable=False)
    Delivery_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Delivery_instruction = db.Column(db.String(400), nullable=True)
    Order_status = db.Column(db.String(20), nullable=False)
    user = db.relationship('User', foreign_keys=[User_id], backref='orders')
    rider = db.relationship('Rider', foreign_keys=[Rider_id], backref='orders')

    def __repr__(self):
        return f"Order('{self.User_id}', '{self.Rider_id}', '{self.Order_status}')"
