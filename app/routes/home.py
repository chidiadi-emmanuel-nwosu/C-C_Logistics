#!/usr/bin/python3
"""index routes"""
from uuid import uuid4
from flask import render_template
from app.routes import app_routes

@app_routes.route("/", strict_slashes=False)
@app_routes.route("/home", strict_slashes=False)
@app_routes.route("/index", strict_slashes=False)
def home():
    """index routes"""
    return render_template("index.html", cache_id=str(uuid4()))
