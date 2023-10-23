#!/usr/bin/python3
"""dashboard routes"""
from uuid import uuid4
from googlemaps import Client
from googlemaps.exceptions import ApiError
from flask import render_template, session, url_for, redirect, flash
from flask_login import login_required, current_user
from app.routes import app_routes
from app.forms.request import RequestForm, CompleteRequest
from app.models.request import DeliveryRequest
from app import db

@app_routes.route("/dashboard", strict_slashes=False)
@login_required
def dashboard():
    """dashboard routes"""
    return render_template("dashboard.html", form=RequestForm(), cache_id=str(uuid4()))

@app_routes.route("/dashboard/account", strict_slashes=False)
@login_required
def dashboard_account():
    """my account routes"""
    return render_template("account.html", dashbard_title="Account Overview", cache_id=str(uuid4()))

@app_routes.route("/dashboard/request", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dashboard_request():
    """request routes"""
    form = RequestForm()
    if form.validate_on_submit():
        session['request_form_data'] = {
                'user_id': current_user.id,
                'pickup_address': form.pickup_address.data,
                'pickup_time': form.pickup_time.data,
                'item_description': form.item_description.data,
                'contact_person': form.contact_person.data,
                'contact_phone_number': form.contact_phone_number.data,
                'delivery_address': form.delivery_address.data,
                'delivery_instruction': form.delivery_instruction.data,
                }
        return redirect(url_for('app_routes.confirm_request'))


    return render_template("request.html", dashbard_title="Request Delivery",
                           form=form, cache_id=str(uuid4()))

@app_routes.route("/dashboard/request/comfirm-request", methods=['GET', 'POST'])
@login_required
def confirm_request():
    """confirm delivery"""
    gmaps = Client(key='AIzaSyBZcq4L2alxdT4eaznBBvWsa9BR266O2kc')

    kwargs = session['request_form_data']
    pickup_address = kwargs['pickup_address']
    delivery_address = kwargs['delivery_address']
    try:
        directions = gmaps.directions(pickup_address, delivery_address, mode="driving")
        direction = directions[0].get('legs')[0]
        if direction:
            cost = calculate_cost(direction['distance']['value'])
            session['request_form_data']['estimated_distance'] = direction['distance']['text']
            session['request_form_data']['estimated_duration'] = direction['duration']['text']
            session['request_form_data']['delivery_cost'] = cost
    except Exception as e:
        if 'NOT_FOUND' in str(e):
            flash("Invalid address. Please enter a valid address or choose from the drop-down suggestions.", "danger")
            return redirect(url_for('app_routes.dashboard_request'))

    form = CompleteRequest()
    if form.validate_on_submit():
        kwargs = session['request_form_data']
        new_request = DeliveryRequest(**kwargs)
        db.session.add(new_request)
        db.session.commit()
        return render_template('confirm_success.html', dashbard_title="Delivery Status")

    return render_template('confirm_request.html', dashbard_title='Confirm Delivery',
                            form=form, direction=direction, cost=cost)


@app_routes.route("/dashboard/deliveries", strict_slashes=False)
@login_required
def dashboard_deliveries():
    """deliveries routes"""
    deliveries = DeliveryRequest.query.filter_by(user_id=current_user.id).all()
    my_deliveries = [i.to_dict() for i in deliveries]
    return render_template("deliveries.html", my_deliveries=my_deliveries,
                           dashbard_title="My Deliveries", cache_id=str(uuid4()))


def calculate_cost(distance):
    """calculate the price of delivery"""
    return 10 * int(distance)
