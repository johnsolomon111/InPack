from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FileField
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
	user_type = StringField('user_type')

class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	rfid = PasswordField('rfid')

class CollegeForm(FlaskForm):
	college_pic = FileField('college_pic', validators=[DataRequired(), Length(min=1,max=200)])
	college_name = StringField('college_name',validators=[DataRequired(), Length(min=1,max=200)])

class CategoryForm(FlaskForm):
	category_name = StringField('category_name', validators=[DataRequired(), Length(min=1,max=50)])

class ItemForm(FlaskForm):
	item_name = StringField('item_name', validators=[DataRequired(),Length(min=1,max=50)])
	quantity = IntegerField('quantity')
	category = StringField('category')

class BorrowForm(FlaskForm):
	quantity = IntegerField('quantity')