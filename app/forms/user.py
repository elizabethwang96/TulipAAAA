from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, DateField, SelectField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

class LoginForm(FlaskForm):
    account = StringField("account", validators=[DataRequired("Please enter your account.")])
    password = PasswordField("password", validators=[DataRequired("Please enter your password.")])