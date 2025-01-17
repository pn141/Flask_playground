from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models.users_model import User


# Registration form that will allow the user to enter its details and for them
# to be kept in our database
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                        Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(),
                           Length(1, 64),
                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                           'Usernames must have only letters, numbers, \
                           dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired(),
                             EqualTo('password2',
                                     message='Password must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')


# Login form to be used once the user has already register
class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(),Length(1,64),
    Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField('Log In')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
                              DataRequired(),
                              EqualTo('password2',
                                      message='Passwords must match.')])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                        Length(1, 64), Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField(
                             'New Password',
                             validators=[DataRequired(), EqualTo('password2',
                                         message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(),
                        Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')
