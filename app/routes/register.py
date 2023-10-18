#!/usr/bin/python3
"""index routes"""
from datetime import datetime
from flask import render_template, flash, url_for, redirect
from app.routes import app_routes
from app.forms.register import RegistrationForm
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db, bcrypt

@app_routes.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """register user or agent"""
    form = RegistrationForm()


    if form.validate_on_submit():
        if form.register_as.data == 'user':
            user_email = User.query.filter_by(email=form.email.data).first()
            user_phone = User.query.filter_by(phone_number=form.phone_number.data).first()

            if user_email:
                flash('Email is already in use. Please choose a different one.', 'danger')
            elif user_phone:
                flash('Phone number is already in use. Please choose a different one.', 'danger')
            else:
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
                )
                db.session.add(new)
                db.session.commit()
                flash('Your user account has been created! You are now able to log in.', 'success')
                return redirect(url_for('app_routes.login'))
        else:
            agent_email = DeliveryAgent.query.filter_by(email=form.email.data).first()
            agent_phone = DeliveryAgent.query.filter_by(phone_number=form.phone_number.data).first()

            if agent_email:
                flash('Email is already in use. Please choose a different one.', 'danger')
            elif agent_phone:
                flash('Phone number is already in use. Please choose a different one.', 'danger')
            else:
                # Create a new DeliveryAgent object and add it to the database
                new = DeliveryAgent (
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    gender=form.gender.data,
                    date_of_birth=datetime.strptime(form.date_of_birth.data, '%d/%m/%Y'),
                    email=form.email.data,
                    password=bcrypt.generate_password_hash(form.password.data),
                    phone_number=form.phone_number.data,
                    contact_address=form.contact_address.data,
                    drivers_license_number=form.drivers_license_number.data,
                    license_expiration_date=datetime.strptime(form.license_expiration_date.data,
                                                              '%d/%m/%Y'),
                    license_image_file=form.license_image_file.data.read()
                )
                db.session.add(new)
                db.session.commit()
                flash('Your account has been created! You are now able to log in.', 'success')
                return redirect(url_for('app_routes.login'))


    return render_template('register.html', form=form, title="Register")
