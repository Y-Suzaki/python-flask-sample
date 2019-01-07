from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    username = StringField('User Name', validators=[
        DataRequired(message='Required field.'),
        Length(max=10, message='Max 10 length.')
    ])

    email = StringField('E-Mail', validators=[
        Email(message='Invalid format.'),
    ])

    password = PasswordField('Password', validators=[
        DataRequired(message='Required field.'),
    ])


class LoginForm(Form):
    username = StringField('User Name', validators=[
        DataRequired(message='Required field.')
    ])

    password = PasswordField('Password', validators=[
        DataRequired(message='Required field.'),
    ])
