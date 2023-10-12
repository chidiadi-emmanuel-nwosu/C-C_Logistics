#!/usr/bin/python3
"""init file"""
from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

from app.routes.index import *
