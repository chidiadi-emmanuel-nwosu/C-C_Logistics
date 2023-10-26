#!/usr/bin/python3
"""dashboard routes"""
from uuid import uuid4
from flask import render_template, url_for, redirect
from flask_login import login_required, current_user
from app.routes import app_routes
from app.forms.update import UpdateAccountForm
from app import db


@app_routes.route("/dashboard/account")
@login_required
def account():
    """my account routes"""
    return render_template("account.html", dashbard_title="Account Overview", cache_id=str(uuid4()))


@app_routes.route('/dashboard/account/edit', methods=['GET','POST'])
@login_required
def update_account():
    """edit the user account"""
    user = current_user
    form = UpdateAccountForm(obj=user)
    if form.validate_on_submit():
        user.phone_number = form.phone_number.data
        user.contact_address = form.contact_address.data
        if user.__class__.__name__ != "User":
            user.drivers_license_number = form.drivers_license_number.data
            user.license_expiration_date = form.license_expiration_date.data
            user.license_image_file = form.license_image_file.data.read()

        db.session.commit()
        return redirect(url_for('app_routes.account'))

    return render_template('update_account.html', form=form,
                           dashbard_title='Update Account', cache_id=str(uuid4()))
