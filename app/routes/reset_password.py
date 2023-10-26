from flask import render_template, flash, url_for, redirect
from app.routes import app_routes
from app.forms.reset_password_form import ResetPasswordForm
from app.models.agent import DeliveryAgent
from app.models.user import User
from app import db, bcrypt, mail
from flask_login import current_user
from app.generate import verify_reset_token

@app_routes.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('app_routes.login'))
    
    form = ResetPasswordForm()

    # Inside the reset_token function

    if form.validate_on_submit():
        try:
            email = verify_reset_token(token)
            if email:
                user = User.query.filter_by(email=email).first()
                rider = DeliveryAgent.query.filter_by(email=email).first()

                if user:
                    hashed_password = bcrypt.generate_password_hash(form.password.data)
                    user.password = hashed_password
                    db.session.commit()
                    flash('Your password has been updated! You are now able to log in', 'success')
                    return redirect(url_for('app_routes.login'))
                elif rider:
                    hashed_password = bcrypt.generate_password_hash(form.password.data)
                    rider.password = hashed_password
                    db.session.commit()
                    flash('Your password has been updated! You are now able to log in', 'success')
                    return redirect(url_for('app_routes.login'))
                else:
                    flash('That is an invalid or expired token', 'warning')
                    return redirect(url_for('app_routes.reset_request'))
            else:
                flash('Invalid or expired token', 'warning')
                return redirect(url_for('app_routes.reset_request'))
        except Exception as e:
            # Log the error and display a user-friendly error message
            print(f"An error occurred: {str(e)}")
            flash('An error occurred while resetting your password. Please try again later.', 'danger')
            return redirect(url_for('app_routes.reset_request'))

        
    return render_template('reset_token.html', title='Reset Password', form=form)
