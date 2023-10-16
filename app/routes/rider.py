#!/usr/bin/python3
"""index routes"""
from flask import render_template, flash, redirect, url_for
from flask_login import login_user
from app.routes import app_routes
from app.forms.login import LoginForm
from app.forms.register import RegistrationForm
from app.models.agent import DeliveryAgent
from app import db, bcrypt


@app_routes.route('/register/rider', methods=['GET', 'POST'])
def register_rider():
    """route for rider registration"""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Similar to user registration but for riders
        rider = Rider(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            date_of_birth=form.date_of_birth.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data),
            phone_number=form.phone_number.data,
            contact_address=form.contact_address.data,
            drivers_license_number=form.drivers_license_number.data,
            license_expiration_date=form.license_expiration_date.data,
            license_image_file=form.license_image_file.data.read()
        )
        db.session.add(rider)
        db.session.commit()
        flash('Your rider account has been created! You are now able to log in.', 'success')
        return redirect(url_for('auth.login_rider'))
    return render_template('register.html', title='Register Rider', form=form)

@app_routes.route('/login/rider', methods=['GET', 'POST'])
def rider_login():
    """route for rider login"""
    form = LoginForm()
    if form.validate_on_submit():
        rider = Rider.query.filter_by(email=form.email.data).first()
        if rider and bcrypt.check_password_hash(form.password.data, rider.password):
            login_user(rider)
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Login Rider', form=form)
