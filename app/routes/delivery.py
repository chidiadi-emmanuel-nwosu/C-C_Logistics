#!/usr/bin/python3
"""dashboard routes"""
from uuid import uuid4
from flask import render_template
from flask_login import login_required, current_user
from app.routes import app_routes
from app.models.request import DeliveryRequest


@app_routes.route("/dashboard/deliveries", strict_slashes=False)
@login_required
def delivery():
    """deliveries routes"""
    deliveries = DeliveryRequest.query.filter_by(user_id=current_user.id).all()
    my_deliveries = [i.to_dict() for i in deliveries]
    return render_template("deliveries.html", my_deliveries=my_deliveries,
                           dashbard_title="My Deliveries", cache_id=str(uuid4()))
