#!/usr/bin/python3
"""earnings routes"""
from uuid import uuid4
from flask import render_template, jsonify, request, flash
from flask_login import login_required, current_user
from app.routes import app_routes


@app_routes.route("/earnings", methods=['GET', 'POST'])
@login_required
def earnings():
    """earnings route"""
    return render_template(
            "earnings.html",
            dashboard_title="My Earnings",
            cache_id=str(uuid4())
            )
