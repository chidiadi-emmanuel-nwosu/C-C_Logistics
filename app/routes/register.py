#!/usr/bin/python3
"""index routes"""
from datetime import datetime
from flask import render_template, flash, url_for, redirect, request
from app.routes import app_routes
from app.forms.register import RegistrationForm
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db, bcrypt, mail
from flask_mail import Message
from app.routes.confirm_email import confirm_email
from app.routes.generate import s
from itsdangerous import URLSafeTimedSerializer
import secrets



@app_routes.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """register user or agent"""
    form = RegistrationForm()

    if form.validate_on_submit():
        user_email = User.query.filter_by(email=form.email.data).first()
        user_phone = User.query.filter_by(phone_number=form.phone_number.data).first()
        agent_email = DeliveryAgent.query.filter_by(email=form.email.data).first()
        agent_phone = DeliveryAgent.query.filter_by(phone_number=form.phone_number.data).first()
        agents_license = DeliveryAgent.query.filter_by(drivers_license_number=form.drivers_license_number.data).first()
        if user_email or agent_email:
            flash('Email is already in use. Please choose a different one.', 'danger')
        elif user_phone or agent_phone:
            flash('Phone number is already in use. Please choose a different one.', 'danger')
        elif agents_license:
            flash('License number is already in use. Please choose a different one.', 'danger')
        elif form.register_as.data == 'user':
            # Create a new User object and add it to the database
            new = User (
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                gender=form.gender.data,
                date_of_birth=datetime.strptime(form.date_of_birth.data, '%d/%m/%Y'),
                email=form.email.data,
                password=bcrypt.generate_password_hash(form.password.data),
                phone_number=form.phone_number.data,
                contact_address=form.contact_address.data,
                is_email_verified=False
            )
            db.session.add(new)
            db.session.commit()

            # Generate a confirmation token and URL
            email = form.email.data
            token = s.dumps(email, salt='email-confirm')
            confirm_url = url_for('app_routes.confirm_email', token=token, _external=True)

            # Send the confirmation email
            msg = Message('Confirm Email', recipients=[email])
            msg.body = 'Your link is {}'.format(confirm_url)
            mail.send(msg)

            flash('Your user account has been created! You are now able to log in.', 'success')
            flash('A confirmation email has been sent via email.', 'success')
            return redirect(url_for('app_routes.login'))

        else:
            # Create a new DeliveryAgent object and add it to the database
            new = DeliveryAgent(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                gender=form.gender.data,
                date_of_birth=datetime.strptime(form.date_of_birth.data, '%d/%m/%Y'),
                email=form.email.data,
                is_email_verified=False,
                password=bcrypt.generate_password_hash(form.password.data),
                phone_number=form.phone_number.data,
                contact_address=form.contact_address.data,
                drivers_license_number=form.drivers_license_number.data,
                license_expiration_date=datetime.strptime(form.license_expiration_date.data, '%d/%m/%Y'),
                license_image_file=form.license_image_file.data.read()
            )
            db.session.add(new)
            db.session.commit()

            # Generate a confirmation token and URL
            email = form.email.data
            token = s.dumps(email, salt='email-confirm')
            confirm_url = url_for('app_routes.confirm_email', token=token, _external=True)

            # Send the confirmation email
            msg = Message('Confirm Email', recipients=[email])
            msg.body = 'Your link is {}'.format(confirm_url)
            mail.send(msg)

            flash('Your user account has been created! You are now able to log in.', 'success')
            flash('A confirmation email has been sent via email.', 'success')
            return redirect(url_for('app_routes.login'))

    return render_template('register.html', form=form, title="Register")
