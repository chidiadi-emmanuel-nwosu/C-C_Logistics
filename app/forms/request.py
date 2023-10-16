from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RequestForm(FlaskForm):
    """request datas from a user"""
    pickup_address = StringField(
        'Pickup Address',
        validators=[DataRequired(), Length(max=200)]
    )
    pickup_time = DateTimeField(
            'Pickup Time', format='%Y-%m-%d %H:%M:%S %f', validators=[DataRequired()]
            )
    item_description = StringField(
        'Item Description',
        validators=[DataRequired(), Length(max=50)]
    )
    delivery_address = StringField(
        'Delivery Address',
        validators=[DataRequired(), Length(max=200)]
    )
    delivery_time = DateTimeField(
            'Delivery Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()]
            )
    delivery_instruction = TextAreaField('Delivery Instructions', validators=[Length(max=400)])
    submit = SubmitField('Submit Order')
