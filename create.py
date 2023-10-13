#!/usr/bin/python3

from app import create_app, db
from app.models import User, Order, Rider  # Import your model classes here

app = create_app('development')  # Use the appropriate configuration
with app.app_context():
    # Create the database tables
    db.create_all()
