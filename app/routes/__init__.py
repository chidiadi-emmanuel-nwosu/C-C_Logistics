#!/usr/bin/python3
"""init file"""
from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

from app.routes.account import *
from app.routes.delivery import *
from app.routes.home import *
from app.routes.register import *
from app.routes.request import *
from app.routes.rider import *
from app.routes.login import *
