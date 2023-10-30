#!/usr/bin/python3
"""index routes"""
from itsdangerous import SignatureExpired, BadData
from flask import flash, url_for, redirect
from app.routes import app_routes
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db
from app.config import serialize_token


@app_routes.route('/confirm_email/<token>')
def confirm_email(token):
    """confirms email address wit sent out token"""

    try:
        email = serialize_token.loads(token, salt='email-confirm',
                                      max_age=10000)
        user = User.query.filter_by(email=email).first()
        agent = DeliveryAgent.query.filter_by(email=email).first()
        get_user = user if user else agent if agent else None

        if get_user:
            if not get_user.is_email_verified:
                get_user.is_email_verified = True
                db.session.commit()
                flash('Email verified. You are now able to login', 'success')
            else:
                flash('account already confirmed.', 'info')
    except [SignatureExpired, BadData]:
        flash('Invalid confirmation link or token is expired. Register again.',
              'danger')
        db.session.delete(get_user)
        db.session.commit()
        return redirect(url_for('app_routes.register'))

    return redirect(url_for('app_routes.login'))
