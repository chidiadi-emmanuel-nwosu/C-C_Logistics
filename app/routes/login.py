from flask import render_template, flash, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from app.routes import app_routes
from app.forms.login import LoginForm
from app.models.user import User
from app.models.agent import DeliveryAgent
from app import bcrypt

@app_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        agent = DeliveryAgent.query.filter_by(email=form.email.data).first()

        if not user and not agent:
            flash('Login unsuccessful. User not found.', 'danger')
        else:
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                if not user.is_email_verified:
                    flash('Please confirm your email before logging in.', 'danger')
                else:
                    login_user(user)
                    flash('Login successful!', 'success')
                    return redirect(url_for('app_routes.dashboard_account'))

            elif agent and bcrypt.check_password_hash(agent.password, form.password.data):
                if not agent.is_email_verified:
                    flash('Please confirm your email before logging in.', 'danger')
                else:
                    login_user(agent)
                    flash('Login successful!', 'success')
                    return redirect(url_for('app_routes.dashboard_account'))

            else:
                flash('Login unsuccessful. Check your email and password.', 'danger')

    return render_template('login.html', title='Login', form=form)


@app_routes.route('/logout')
# @login_required
def logout():
    """route for user logout"""
    logout_user()
    return redirect(url_for('app_routes.home'))
