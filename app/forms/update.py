#!/usr/bin/python3
"""edit form module"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, PasswordField
from wtforms.validators import DataRequired, Regexp


class UpdateAccountForm(FlaskForm):
    """Rider registration form"""

    register_as = StringField('Register As')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_of_birth = StringField('Date of Birth')
    gender = StringField('Gender')
    email = StringField('Email')
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    contact_address = StringField('Contact Address', validators=[DataRequired()])
    drivers_license_number = StringField(
            "Driver's License Number",
            validators=[Regexp(r'^[A-Z0-9]*$', message='Invalid license number format')]
        )
    license_expiration_date = StringField('License Expiration Date')
    license_image_file = FileField('License Image File')
    password = PasswordField('Password')
    submit = SubmitField('Update Account')
