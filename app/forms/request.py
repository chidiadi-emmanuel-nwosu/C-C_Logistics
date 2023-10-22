#!/usr/bin/python3
"""registration forms module"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Regexp
from wtforms.fields import DateTimeLocalField


class RequestForm(FlaskForm):
    """request datas from a user"""
    pickup_address = StringField('Pickup Address',
                                 validators=[DataRequired(), Length(max=200)])
    set_default_pickup = BooleanField('Use contact address as pickup address')
    delivery_address = StringField('Delivery Address',
                                   validators=[DataRequired(), Length(max=200)])
    set_default_delivery = BooleanField('Use contact address as delivery address')
    item_description = StringField('Item Description',
                                   validators=[DataRequired(), Length(max=50)])
    contact_person = StringField('Name of Contact Person',
                                   validators=[DataRequired(), Length(max=50)])
    contact_phone_number = StringField(
        'Contact Phone Number',
        validators=[
            DataRequired(message='Phone number is required'),
            Regexp(r'^[0-9]{11}$', message='Invalid phone number format. Use 11 digits only.')
        ]
    )
    delivery_instruction = TextAreaField('Delivery Instructions', validators=[Length(max=400)])
    set_pickup_time = BooleanField('Add a pickup time')
    pickup_time = DateTimeLocalField('Pickup Time', format='%Y-%m-%d %H:%M:%S %f',
                                validators=[Optional()])
    submit = SubmitField('Submit Delivery')


class CompleteRequest(FlaskForm):
    """complet request foam"""
    submit = SubmitField('Confirm Delivery')
