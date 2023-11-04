#!/usr/bin/python3
"""accept request"""
from flask import jsonify, request, flash
from flask_login import login_required, current_user
from app.routes import app_routes
from app.models.request import DeliveryRequest
from app import db


@app_routes.route("/dashboard/delivered", methods=['POST'])
@login_required
def delivered():
    """deliveries routes"""
    delivery_id = request.form.get('delivery_id')
    delivery_ = DeliveryRequest.query.filter_by(id=delivery_id).first()
    if delivery_:
        try:
            delivery_.agent_id = current_user.id
            delivery_.order_status = 'Delivered'
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            flash('Error occured')
    return jsonify({'success': False})
