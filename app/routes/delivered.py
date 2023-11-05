#!/usr/bin/python3
"""accept request"""
from flask import jsonify, request, flash
from flask_login import login_required
from flask_mail import Message
from app.routes import app_routes
from app.models.request import DeliveryRequest
from app.models.user import User
from app import db, mail


@app_routes.route("/dashboard/delivered", methods=['POST'])
@login_required
def delivered():
    """deliveries routes"""
    delivery_id = request.form.get('delivery_id')
    delivery_data = DeliveryRequest.query.filter_by(id=delivery_id).first()
    if delivery_data:
        try:
            delivery_data.order_status = 'Delivered'
            db.session.commit()

            user_id = delivery_data.user_id
            user = User.query.filter_by(id=user_id).first()
            email = user.email
            msg = Message('Parcel Delivered', recipients=[email])
            msg.body = f"""Your parcel with id {delivery_data.id} has been delivered successfully.

Contact person: {delivery_data.contact_person}.
Contact phone number: {delivery_data.contact_phone_number}."""
            mail.send(msg)
            flash("An email has been sent to the user", 'success')

            return jsonify({'success': True})
        except Exception as e:
            flash(f'could not send delivered email. Error: {e}', 'danger')
    return jsonify({'success': False})
