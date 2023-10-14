#!/usr/bin/python3
"""register user module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from app.models.user import User


class UserRegistrationForm(FlaskForm):
    """user registration form"""
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
                Length(min=3, max=20, message="Please enter a valid name"),
                Regexp(
                    r'^[A-Za-z\s\-\']+$',
                    message='Invalid name format. Use letters, spaces, and hyphens only.'
                    )
                ]
            )
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=72)])
    confrim_password = PasswordField(
            'Confirm Password',
            validators=[
                DataRequired(),
                EqualTo('password', message="password does not match!")
                ]
            )
    phone_number = StringField(
            'Phone Number',
            validators=[
                DataRequired(message='Phone number is required'),
                Regexp(
                    r'^[0-9]{11}$',
                    message='Invalid phone number format. Use 11 digits only.'
                    )
                ]
            )
    submit = SubmitField('Sign Up')



    def validate_email(self, email):
        """checks if the email already exist in the db"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use. Please choose a different one.')

    def validate_phone_number(self, phone_number):
        """checks if the phone already exist in the db"""
        user = User.query.filter_by(phone_number=phone_number.data).first()
        if user:
            raise ValidationError('Phone number is already in use. Please choose a different one.')
