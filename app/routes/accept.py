#!/usr/bin/python3
"""accept request"""
from uuid import uuid4
from flask import render_template, jsonify, request, flash
from flask_login import login_required, current_user
from flask_mail import Message
from app.routes import app_routes
from app.models.agent import DeliveryAgent
from app.models.request import DeliveryRequest
from app.models.user import User
from app import db, mail


@app_routes.route("/dashboard/accept-delivery", methods=['GET', 'POST'])
@login_required
def accept_delivery():
    """deliveries routes"""
    if request.method == 'POST':
        delivery_id = request.form.get('delivery_id')
        delivery_data = DeliveryRequest.query.filter_by(id=delivery_id).first()
        if delivery_data:
            try:
                delivery_data.agent_id = current_user.id
                delivery_data.order_status = 'Delivery Accepted'
                db.session.commit()

                user_id = delivery_data.user_id
                agent_id = delivery_data.agent_id
                user = User.query.filter_by(id=user_id).first()
                agent = DeliveryAgent.query.filter_by(id=agent_id).first()
                email = user.email
                msg = Message('Delivery request accepted', recipients=[email])
                msg.body = f"""Your delivery request with id {delivery_data.id} has been accepted and a delivery agent is on his way.
                                Agent name: {agent.first_name} {agent.last_name}.
                                Agent phone number: {agent.phone_number}.
                            """
                mail.send(msg)
                flash("An email has been sent to the user", 'success')

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
