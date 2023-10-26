#!/usr/bin/python3
"""index routes"""
from flask import render_template, flash, url_for, redirect, request
from app.routes import app_routes
from app.forms.request_reset_form import RequestResetForm
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db, bcrypt, mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadData
from flask_mail import Message
from app.config import config
from flask_login import login_required, current_user
from flask import current_app
from itsdangerous import URLSafeTimedSerializer
from app.generate import s

# Access the app object

@app_routes.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        agent = DeliveryAgent.query.filter_by(email=email).first()

        if user:
            token = s.dumps(email, salt='reset-password')
            msg = Message('Password Reset Request',
                          recipients=[email])
            link = url_for('app_routes.reset_token', token=token, _external=True)
            msg.body = f'''To reset your password, visit the following link:
{link}

If you did not make this request then simply ignore this email, and no changes will be made.
'''
            try:
                mail.send(msg)
                flash('An email has been sent with instructions to reset your password.', 'success')
            except Exception as e:
                flash('An error occurred while sending the email. Please try again later.', 'danger')
            return redirect(url_for('app_routes.login'))
        elif agent:
            token = s.dumps(email, salt='reset-password')
            msg = Message('Password Reset Request',
                          recipients=[email])
            link = url_for('app_routes.reset_token', token=token, _external=True)
            msg.body = f'''To reset your password, visit the following link:
{link}

If you did not make this request then simply ignore this email, and no changes will be made.
'''
            try:
                mail.send(msg)
                flash('An email has been sent with instructions to reset your password.', 'success')
            except Exception as e:
                flash('An error occurred while sending the email. Please try again later.', 'danger')
            return redirect(url_for('app_routes.login'))
        else:
            # Handle the case when no user or agent with the provided email is found
            flash('No user or agent found with the provided email address.', 'danger')

    return render_template('reset_request.html', title='Reset Password', form=form)
