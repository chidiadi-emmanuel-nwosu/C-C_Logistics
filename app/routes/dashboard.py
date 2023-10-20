#!/usr/bin/python3
"""index routes"""
from uuid import uuid4
from flask import render_template, jsonify,request
from flask_login import login_required
from app.routes import app_routes
from app.forms.request import RequestForm
import requests

@app_routes.route("/dashboard", strict_slashes=False)
def dashboard():
    """dashboard routes"""
    return render_template("dashboard.html", form=RequestForm(), cache_id=str(uuid4()))

@app_routes.route("/dashboard/account", strict_slashes=False)
def dashboard_account():
    """my account routes"""
    return render_template("dashboard_account.html", dashbard_title="Account Overview", cache_id=str(uuid4()))

@app_routes.route("/dashboard/request", strict_slashes=False)
def dashboard_request():
    """request routes"""
    return render_template("dashboard_request.html", dashbard_title="Request Delivery", form=RequestForm(), cache_id=str(uuid4()))


@app_routes.route('/calculate_route', methods=['POST'])
def calculate_route():
    origin = request.form.get('pickup_address')
    destination = request.form.get('delivery_address')

    # Ensure that you have defined API_KEY with your Google Maps API Key
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_key}'
    response = requests.get(url)
    data = response.json()

    # Check if the request was successful
    if data['status'] == 'OK':
        # Extract distance and duration information
        route = data['routes'][0]
        leg = route['legs'][0]
        distance = leg['distance']['text']  # The distance in human-readable format
        duration = leg['duration']['text']  # The duration in human-readable format

        response_data = {
            'distance': distance,
            'duration': duration,
        }

        return jsonify(response_data)
    else:
        return jsonify({'error': 'Unable to calculate distance and duration'})


@app_routes.route("/dashboard/deliveries", strict_slashes=False)
def dashboard_deliveries():
    """deliveries routes"""
    return render_template("dashboard_deliveries.html", dashbard_title="My Deliveries", cache_id=str(uuid4()))
