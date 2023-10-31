#!/usr/bin/python3
"""accept request"""
from uuid import uuid4
from flask import render_template, jsonify, request, flash
from flask_login import login_required, current_user
from app.routes import app_routes
from app.models.agent import DeliveryAgent
from app.models.request import DeliveryRequest
from app.models.user import User
from app import db,mail
from flask_mail import Message 
import notify2


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

                # Retrieve delivery data and user information
                delivery_data = DeliveryRequest.query.filter_by(id=delivery_id).first()
                if delivery_data:
                    user_id = delivery_data.user_id
                    agent_id = delivery_data.agent_id
                    user = User.query.filter_by(id=user_id).first()
                    rider = DeliveryAgent.query.filter_by(id=agent_id).first()
                    email = user.email
                    msg = Message('Order accepted', recipients=[email])
                    msg.body = f"""Your rider is on his way. These are his details {rider.first_name} {rider.last_name}.
                                    You can reach them with this phone number: {rider.phone_number}."""
                    mail.send(msg)
                    flash("An email has been sent to the user", 'success')

                    if user:
                        notify2.init("C&C logistics")
                        message = f"""You have accepted to deliver an item for {user.first_name} {user.last_name}.
                        You can reach them with this phone number: {user.phone_number}."""
                        n = notify2.Notification("Order notification", message)
                        n.show()

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
            dashboard_title="My Deliveries",
            cache_id=str(uuid4())
            )