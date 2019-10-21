from app import *

from flask import render_template, request, redirect, url_for

@server.route('/', methods=["GET","POST"])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		return 'username: {} rfid: {}'.format(form.username.data, form.rfid.data)
	return render_template('index.html', title="Inpack", form=form)

@server.route('/login', methods=["GET", "POST"])
def login_with_password():
	form = LoginForm()
	if form.validate_on_submit():
		return 'username: {} password: {}'.format(form.username.data, form.password.data)
	return render_template('login.html', title="Log In with Password", form=form)

@server.route('/signup', methods=["GET", "POST"])
def signup():
	form = RegistrationForm()
	if form.validate_on_submit():
		new_user = User(form.contact.data, form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, form.rfid.data)
		dbase.session.add(new_user)
		dbase.session.commit()

		# return 'contact: {} firstname: {} lastname: {} email: {} username: {} password: {} confirm: {} rfid: {}'.format(form.contact.data, form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, form.confirm.data, form.rfid.data)
		return redirect(url_for('dashboard'))
	return render_template('signup.html', title="Get Started!", form=form)

@server.route('/dashboard', methods=["GET", "POST"])
def dashboard():
	return render_template('dashboard.html', title="Dashboard")