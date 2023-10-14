#!/usr/bin/python3
"""index routes"""
from flask import render_template, flash, redirect, url_for
from flask_login import login_user
from app.routes import app_routes
from app.forms.login_user import UserLoginForm
from app.forms.register_user import UserRegistrationForm
from app.models.user import User
from app import db, bcrypt


@app_routes.route('/register/user', methods=['GET', 'POST'], strict_slashes=False)
def register_user():
    """route for user registration"""
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data),
            phone_number=form.phone_number.data,
            user_type='user'
        )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login_user'))
    return render_template('register.html', title='Register User', form=form)

@app_routes.route('/login/user', methods=['GET', 'POST'])
def user_login():
    """route for user login"""
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(form.password.data, user.password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('user_dashboad'))
        flash('Login unsuccessful. Check your email and password.', 'danger')
    return render_template('login.html', title='Login User', form=form)
