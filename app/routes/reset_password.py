#!/usr/bin/python3
"""index routes"""
from itsdangerous import SignatureExpired, BadData
from flask import render_template, flash, url_for, redirect
from flask_mail import Message
from flask_login import current_user
from app.routes import app_routes
from app.forms.reset import RequestResetForm, ResetPasswordForm
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db, bcrypt, mail
from app.config import serialize_token


@app_routes.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    """reset password"""
    form = RequestResetForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        agent = DeliveryAgent.query.filter_by(email=email).first()

        if user or agent:
            token = serialize_token.dumps(email, salt='reset-password')
            msg = Message('Password Reset Request', recipients=[email])
            link = url_for('app_routes.reset_token', token=token, _external=True)
            msg.body = (f'''To reset your password, visit the following link: 
{link}

If you did not make this request then simply ignore this email, and no changes will be made.''')
            try:
                mail.send(msg)
                flash('An email has been sent with instructions to reset your password.', 'success')
            except [BadData, SignatureExpired]:
                flash('An error occurred while sending the email. Please try again later.',
                      'danger')
            return redirect(url_for('app_routes.login'))
        flash('No user or agent found with the provided email address.', 'danger')

    return render_template('reset_request.html', title='Reset Password', form=form)


@app_routes.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    """reset password token"""
    if current_user.is_authenticated:
        return redirect(url_for('app_routes.login'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        try:
            email = serialize_token.loads(token, salt='reset-password', max_age=10000)
            if email:
                user = User.query.filter_by(email=email).first()
                agent = DeliveryAgent.query.filter_by(email=email).first()
                get_user = user if user else agent if agent else None

                if get_user:
                    hashed_password = bcrypt.generate_password_hash(form.password.data)
                    get_user.password = hashed_password
                    db.session.commit()
                    flash('Your password has been updated! You are now able to log in', 'success')
                    return redirect(url_for('app_routes.login'))

                flash('Invalid or expired token', 'danger')
                return redirect(url_for('app_routes.reset_request'))

            flash('Invalid or expired token', 'danger')
            return redirect(url_for('app_routes.reset_request'))
        except [BadData, SignatureExpired]:
            flash('An error occurred while resetting your password. Please try again later or contact support.',
                  'danger')
            return redirect(url_for('app_routes.reset_request'))

    return render_template('reset_token.html', title='Reset Password', form=form)
