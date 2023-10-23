#!/usr/bin/python3
"""index routes"""
from datetime import datetime
from flask import render_template, flash, url_for, redirect, request
from app.routes import app_routes
from app.forms.register import RegistrationForm
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db, bcrypt, mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadData
from flask_mail import Message
from app.config import config
from flask_login import login_required, current_user
import secrets
from app.routes.generate import confirm_token


s = URLSafeTimedSerializer(secrets.token_hex(16))

@app_routes.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
        user = User.query.filter_by(email=email).first()
        rider = DeliveryAgent.query.filter_by(email=email).first()

        if user:
            if not user.is_email_verified:
                user.is_email_verified = True
                db.session.commit()
                flash('You have confirmed your user account. Thanks!', 'success')
            else:
                flash('User account already confirmed.', 'info')
        elif rider:
            if not rider.is_email_verified:
                rider.is_email_verified = True
                db.session.commit()
                flash('You have confirmed your agent account. Thanks!', 'success')
            else:
                flash('Agent account already confirmed.', 'info')
        else:
            flash('Invalid confirmation link.', 'danger')
    except SignatureExpired:
        flash('The token is expired!', 'danger')
    except BadData:
        flash('Invalid confirmation link.', 'danger')

    return redirect(url_for('app_routes.login'))