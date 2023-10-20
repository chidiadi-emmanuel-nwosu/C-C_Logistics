#!/usr/bin/python3
"""init file"""
from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

from app.routes.home import *
from app.routes.register import *
from app.routes.rider import *
from app.routes.login import *
from app.routes.dashboard import *
