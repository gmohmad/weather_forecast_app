from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    comfortable_temperature = IntegerField('Comfortable Temperature', validators=[DataRequired()])
    submit = SubmitField('Sign Up')