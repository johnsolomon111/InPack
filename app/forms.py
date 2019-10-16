from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegistrationForm(FlaskForm):
	contact = StringField('contact')
	firstname = StringField('firstname')
	lastname = StringField('lastname')
	email = StringField('email')
	username = StringField('username')
	password = PasswordField('password')
	confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
	rfid = PasswordField('rfid')