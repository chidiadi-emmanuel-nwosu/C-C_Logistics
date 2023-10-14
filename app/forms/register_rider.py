#!/usr/bin/python3
"""forms module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FileField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from app.models.rider import Rider


class RiderRegistrationForm(FlaskForm):
    """Rider registration form"""
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(),
            Length(min=3, max=20, message="Please enter a valid name"),
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
            Length(min=3, max=30, message="Please enter a valid name"),
            Regexp(
                r'^[A-Za-z\s\-\']+$',
                message='Invalid name format. Use letters, spaces, and hyphens only.'
            )
        ]
    )
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired(), Length(max=20)])
    marital_status = StringField('Marital Status', validators=[Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=72)])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', message="Passwords do not match")]
    )
    phone_number = StringField(
        'Phone Number',
        validators=[
            DataRequired(message='Phone number is required'),
            Regexp(r'^[0-9]{11}$', message='Invalid phone number format. Use 11 digits only.')
        ]
    )
    contact_address = StringField('Contact Address', validators=[DataRequired(), Length(max=80)])
    drivers_license_number = StringField(
        "Driver's License Number",
        validators=[
            DataRequired(),
            Length(max=10),
            Regexp(r'^[A-Z0-9]*$', message='Invalid license number format')
            ]
        )
    license_expiration_date = DateField('License Expiration Date', validators=[DataRequired()])
    license_image_file = FileField(
        'License Image File',
        validators=[DataRequired(), Length(max=20)]
    )
    submit = SubmitField('Sign Up')


    def validate_email(self, email):
        """checks if the email already exist in the db"""
        rider = Rider.query.filter_by(email=email.data).first()
        if rider:
            raise ValidationError('Email is already in use. Please choose a different one.')

    def validate_phone_number(self, phone_number):
        """checks if the phone already exist in the db"""
        rider = Rider.query.filter_by(phone_number=phone_number.data).first()
        if rider:
            raise ValidationError('Phone number is already in use. Please choose a different one.')
