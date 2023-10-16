#!/usr/bin/python3
"""index routes"""
from flask import render_template, flash, redirect, url_for
from flask_login import login_user
from app.routes import app_routes
from app.forms.login import LoginForm
from app.models.user import User
from app.models.agent import DeliveryAgent
from app import bcrypt


@app_routes.route('/login', methods=['GET', 'POST'])
def login():
    """route for user login"""
    form = LoginForm()
    if form.validate_on_submit():
        if form.login_as.data == 'user':
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(form.password.data, user.password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('user_dashboad'))
            flash('Login user unsuccessful. Check your email and password.', 'danger')
        else:
            agent = DeliveryAgent.query.filter_by(email=form.email.data).first()
            if agent and bcrypt.check_password_hash(form.password.data, user.password):
                login_user(agent)
                flash('Login successful!', 'success')
                return redirect(url_for('agent_dashboad'))
            flash('Login agent unsuccessful. Check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
