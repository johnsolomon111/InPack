from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField,SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RegistrationForm(FlaskForm):
	contact = StringField('contact', validators=[DataRequired(), Length(min=11,max=15)]) #max 11
	firstname = StringField('firstname') 
	lastname = StringField('lastname')
	email = StringField('email')
	username = StringField('username', validators=[DataRequired(), Length(min=4,max=20)]) #min4 max 20
	password = PasswordField('password', validators=[DataRequired(), Length(min=6,max=50)]) #min 6 #max 50
	confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
	rfid = PasswordField('rfid')

class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	rfid = PasswordField('rfid')

class ItemForm(FlaskForm):
    categories = [('Sports', 'Sports'),
                   ('Literary', 'Literary'),
                   ('Cultural', 'Cultural'),
				   ('Special Com','Special Com'),
				   ('Facilities Com','Facilities Com')]
    item_name = StringField('Item')
    statuses = [('Available', 'Available'),
            ('Not Available', 'Not Available')]
    quantity = StringField('Quantity')
    category = SelectField('Category', choices = categories)
    status = SelectField('Status', choices = statuses)
    submit = SubmitField('Submit')
