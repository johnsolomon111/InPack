from app import *

from flask import render_template, request, redirect, url_for

@server.route('/', methods=["GET"])
def index():
	print('zzzzzzzzz')
	return render_template('index.html', title="Inpack")

@server.route('/login', methods=["GET"])
def login_with_password():
	return render_template('login.html', title="Log In with Password")

@server.route('/signup', methods=["GET", "POST"])
def signup():
	form = RegistrationForm()
	print(form)
	if form.validate_on_submit():
		return redirect(url_for('dashboard'))
	return render_template('signup2.html', title="Get Started!", form=form)

@server.route('/dashboard', methods=["GET", "POST"])
def dashboard():
	return render_template('dashboard.html', title="Dashboard")






@server.route('/results', methods=["POST"])
def results():
	contact = request.form['contact']
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
	rpassword = request.form['rpassword']
	rfid = request.form['rfid']
	return 'contact: ' + contact + 'firstname: ' + firstname + 'lastname: ' +lastname+ 'email: '+email+'username: '+ username+'password: '+ password+ 'rpassword: '+ rpassword+'rfid: '+rfid

