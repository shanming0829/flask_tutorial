from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """docstring for LoginForm"""
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class LoginUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Username is needed.')])
    password = PasswordField('Password', validators=[DataRequired('Username is needed.')])
    remember_me = BooleanField('remember_me', default=False)
