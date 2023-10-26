#!/usr/bin/python3
from uuid import uuid4
from flask import render_template, jsonify, request, flash
from flask_login import login_required, current_user
from app.routes import app_routes
from app.models.request import DeliveryRequest
from app import db

@app_routes.route("/dashboard/deliveries")
@login_required
def delivery():
    """deliveries routes"""
    deliveries = DeliveryRequest.query.filter_by(user_id=current_user.id).all()
    my_deliveries = [delivery.to_dict() for delivery in deliveries]
    return render_template("deliveries.html", my_deliveries=my_deliveries,
                           dashbard_title="My Deliveries", cache_id=str(uuid4()))

@app_routes.route("/delete_delivery", methods=['POST'])
@login_required
def delete_delivery():
    """delete deliveries routes"""
    delivery_id = request.form.get('delivery_id')
    delivery_ = DeliveryRequest.query.filter_by(id=delivery_id).first()

    if delivery_:
        try:
            db.session.delete(delivery_)
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            flash('Failed to delete delivery')
    return jsonify({'success': False})
