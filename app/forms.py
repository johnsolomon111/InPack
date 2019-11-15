from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SelectField, SubmitField
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
                   ('Cultural', 'Cultural')]
    item_name = StringField('Item')
    statuses = [('Available', 'Available'),
            ('Not Available', 'Not Available')]
    quantity = StringField('Quantity')
    category = SelectField('Category', choices = categories)
    status = SelectField('Status', choices = statuses)
    submit = SubmitField('Submit')

class BorrowForm(FlaskForm):
	borrow_fname = StringField('First Name')
	borrow_lname = StringField('Last Name')
	borrow_idno = StringField('Student ID No.')
	borrow_colleges = [('CCS', 'CCS'), ('CBAA', 'CBAA'), ('CASS', 'CASS'), ('CSM', 'CSM'), ('COET', 'COET'), ('CON', 'CON'), ('CED', 'CED')]
	borrow_course = StringField('Course')
	borrow_statuses = [('Borrowed', 'Borrowed'), ('Returned', 'Returned')]
	borrow_college =  SelectField('Colleges', choices = borrow_colleges)
	borrow_status =  SelectField('Status', choices = borrow_statuses)
	item_id = StringField('Item No.')
	submit = SubmitField('Submit')