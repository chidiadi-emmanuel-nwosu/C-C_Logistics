#!/usr/bin/python3
"""accept request"""
from uuid import uuid4
from flask import render_template, jsonify, request, flash
from flask_login import login_required, current_user
from app.routes import app_routes
from app.models.request import DeliveryRequest
from app.models.user import User
from app import db


@app_routes.route("/dashboard/accept-delivery", methods=['GET', 'POST'])
@login_required
def accept_delivery():
    """deliveries routes"""
    if request.method == 'POST':
        delivery_id = request.form.get('delivery_id')
        delivery_ = DeliveryRequest.query.filter_by(id=delivery_id).first()
        if delivery_:
            try:
                delivery_.agent_id = current_user.id
                delivery_.order_status = 'Delivery Accepted'
                db.session.commit()
                return jsonify({'success': True})
            except Exception as e:
                flash('Error occured while accept delivery')
        return jsonify({'success': False})

    deliveries = DeliveryRequest.query.filter_by(order_status="pending").all()
    my_deliveries = [delivery.to_dict() for delivery in deliveries]

    get_users = User.query.all()
    users = [user.to_dict() for user in get_users]
    return render_template(
            "accept.html",
            my_deliveries=my_deliveries,
            users=users,
            dashboard_title="Accept Delivery Request",
            cache_id=str(uuid4())
            )
