#!/usr/bin/python3
"""index routes"""
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
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
        user = User.query.filter_by(email=form.email.data).first()
        agent = DeliveryAgent.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login user successful!', 'success')
            return redirect(url_for('app_routes.dashboard_account'))
        if agent and bcrypt.check_password_hash(agent.password, form.password.data):
            login_user(agent)
            flash('Login agent successful!', 'success')
            return redirect(url_for('app_routes.dashboard_account'))
        flash('Login unsuccessful. Check your email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app_routes.route('/logout')
# @login_required
def logout():
    """route for user logout"""
    logout_user()
    return redirect(url_for('app_routes.home'))
