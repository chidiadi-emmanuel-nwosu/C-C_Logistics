from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Optional
from wtforms.fields import DateTimeLocalField

class RequestForm(FlaskForm):
    """request datas from a user"""
    pickup_address = StringField('Pickup Address',
                                 validators=[DataRequired(), Length(max=200)])
    delivery_address = StringField('Delivery Address',
                                   validators=[DataRequired(), Length(max=200)])
    item_description = StringField('Item Description',
                                   validators=[DataRequired(), Length(max=50)])
    delivery_instruction = TextAreaField('Delivery Instructions', validators=[Length(max=400)])
    set_pickup_time = BooleanField('Add a pickup time')
    pickup_time = DateTimeLocalField('Pickup Time', format='%Y-%m-%d %H:%M:%S %f',
                                validators=[Optional()])
    submit = SubmitField('Confirm Delivery')
