#!/usr/bin/python3
"""forms module"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    """login form"""
    # login_as = SelectField(
    #         'Register As',
    #         choices=[('user', 'User'), ('delivery agent', 'Delivery Agent')],
    #         validators=[DataRequired()]
    #         )
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
            'Password', validators=[DataRequired(), Length(min=8, max=72)]
            )
    submit = SubmitField('Login')
