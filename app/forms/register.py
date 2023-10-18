#!/usr/bin/python3
"""forms module"""

from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError


class RegistrationForm(FlaskForm):
    """Rider registration form"""

    register_as = SelectField(
            'Register As',
            choices=[('user', 'User'), ('delivery agent', 'Delivery Agent')],
            validators=[DataRequired()]
            )
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(),
            Length(min=2, max=30, message="Please enter a valid name"),
            Regexp(
                r'^[A-Za-z\s\-\']+$',
                message='Invalid name format. Use letters, spaces, and hyphens only.'
            )
        ]
    )
    last_name = StringField(
        'Last Name',
        validators=[
            DataRequired(),
            Length(min=2, max=30, message="Please enter a valid name"),
            Regexp(
                r'^[A-Za-z\s\-\']+$',
                message='Invalid name format. Use letters, spaces, and hyphens only.'
            )
        ]
    )
    date_of_birth = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField(
            'Gender',
            choices=[('male', 'Male'), ('female', 'Female')],
            validators=[DataRequired()]
            )
    marital_status = StringField('Marital Status', validators=[Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    phone_number = StringField(
        'Phone Number',
        validators=[
            DataRequired(message='Phone number is required'),
            Regexp(r'^[0-9]{11}$', message='Invalid phone number format. Use 11 digits only.')
        ]
    )
    contact_address = StringField('Contact Address', validators=[DataRequired(), Length(max=300)])
    drivers_license_number = StringField(
            "Driver's License Number",
            validators=[Regexp(r'^[A-Z0-9]*$', message='Invalid license number format')]
        )
    license_expiration_date = StringField('License Expiration Date')
    license_image_file = FileField('License Image File')
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=8, message='password field should be at least 8 characters')])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message="Passwords do not match")])
    submit = SubmitField('Sign Up')


    def validate_date_of_birth(self, field):
        """validates date of birth"""
        try:
            date_format = '%d/%m/%Y'
            date = datetime.strptime(field.data, date_format)
            field.data = date.strftime(date_format)
        except ValueError:
            raise ValidationError('Invalid birth date format. Use dd/mm/yyyy.')

    def validate_license_expiration_date(self, field):
        """validates license expiration date"""
        try:
            date_format = '%d/%m/%Y'
            date = datetime.strptime(field.data, date_format)
            field.data = date.strftime(date_format)
        except ValueError:
            raise ValidationError('Invalid license date format. Use dd/mm/yyyy.')
