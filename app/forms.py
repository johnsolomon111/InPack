from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class RegistrationForm(FlaskForm):
	contact = StringField('contact')
	firstname = StringField('firstname')
	lastname = StringField('lastname')
	email = StringField('email')
	username = StringField('username')
	password = PasswordField('password')
	confirm = PasswordField('confirm')
	rfid = PasswordField('rfid')