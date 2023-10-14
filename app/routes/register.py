#!/usr/bin/python3
"""index routes"""
from flask import render_template
from app.routes import app_routes

@app_routes.route('/register', strict_slashes=False)
def register():
    """register route to select either user or rider"""
    return render_template('register.html', title="Register")
