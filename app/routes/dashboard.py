#!/usr/bin/python3
"""index routes"""
from uuid import uuid4
from flask import render_template
from flask_login import login_required
from app.routes import app_routes
from app.forms.request import RequestForm

@app_routes.route("/dashboard", strict_slashes=False)
def dashboard():
    """dashboard routes"""
    return render_template("dashboard.html", form=RequestForm(), cache_id=str(uuid4()))

@app_routes.route("/dashboard/account", strict_slashes=False)
def dashboard_account():
    """my account routes"""
    return render_template("dashboard_account.html", dashbard_title="Account Overview", cache_id=str(uuid4()))

@app_routes.route("/dashboard/request", strict_slashes=False)
def dashboard_request():
    """request routes"""
    return render_template("dashboard_request.html", dashbard_title="Request Delivery", form=RequestForm(), cache_id=str(uuid4()))

@app_routes.route("/dashboard/deliveries", strict_slashes=False)
def dashboard_deliveries():
    """deliveries routes"""
    return render_template("dashboard_deliveries.html", dashbard_title="My Deliveries", cache_id=str(uuid4()))
