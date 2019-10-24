from app import *

from flask import render_template, request, redirect, url_for, flash

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@server.route('/', methods=["GET","POST"])
def index():
	form = LoginForm()
	if current_user.is_authenticated is True:
		return redirect(url_for('dashboard'))
	elif form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.rfid, form.rfid.data):
				login_user(user)
				return redirect(url_for('dashboard'))
			else:
				flash('Invalid username or password')
				return render_template('index.html', form=form, title="Inpack")
		else:
			return render_template('index.html', form=form, title="Inpack")
	return render_template('index.html', title="Inpack", form=form)

@server.route('/login', methods=["GET", "POST"])
def login_with_password():
	form = LoginForm()
	if current_user.is_authenticated is True:
		return redirect(url_for('dashboard'))
	elif form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				return redirect(url_for('dashboard'))
			else:
				flash('Invalid username or password')
				return render_template('login.html', form=form, title="Log In with Password")
		else:
			return render_template('login.html', title="Log In with Password", form=form)
	return render_template('login.html', title="Log In with Password", form=form)

@server.route('/signup', methods=["GET", "POST"])
def signup():
	form = RegistrationForm()
	if current_user.is_authenticated is True:
		return redirect(url_for('dashboard'))
	elif form.validate_on_submit():
		new_user = User(form.contact.data, form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, form.rfid.data)
		dbase.session.add(new_user)
		dbase.session.commit()

		user = User.query.filter_by(username=form.username.data).first()
		login_user(user)
		return redirect(url_for('dashboard'))
	else:
		return render_template('signup.html', title="Get Started!", form=form)
	return render_template('signup.html', title="Get Started!", form=form)

@server.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
	user = current_user
	return render_template('dashboard.html', title="Dashboard", user=user)

@server.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))