#!/usr/bin/python3
"""routes"""
from flask import render_template
from app.routes import app_routes

@app_routes.route("/")
@app_routes.route("/index")
def index():
    """index routes"""
    return render_template("index.html")
