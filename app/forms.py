from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    IntegerField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import (
    ValidationError,
    DataRequired,
    Email,
    EqualTo
)

from app.models import User


class LoginForm(FlaskForm):
    """ 
    Form for login
    """

    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
    """
    Form for register
    """

    username = StringField('Username', validators=[DataRequired()])

    comfortable_temperature = IntegerField(
        'Comfortable Temperature',
        validators=[DataRequired()]
    )

    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    password2 = PasswordField(
        'Repeat Password',
        validators=[DataRequired(),
        EqualTo('password')]
    )

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """
        Validate email
        """

        user = User.query.filter_by(email=email.data).first()

        if user is not None:
            raise ValidationError('Please use a different email address.')
