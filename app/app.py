from app import *

from flask import render_template, request, redirect, url_for, flash, request

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
				return render_template('index.html', form=form, title="InPack")
		else:
			return render_template('index.html', form=form, title="InPack")
	return render_template('index.html', title="InPack", form=form)

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
		new_user = User(form.contact.data, form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, form.rfid.data, 'Admin')
		dbase.session.add(new_user)
		dbase.session.commit()
		user = User.query.filter_by(username=form.username.data).first()
		login_user(user)
		return redirect(url_for('college'))
	else:
		return render_template('signup.html', title="Get Started!", form=form)
	return render_template('signup.html', title="Get Started!", form=form)

@server.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	return render_template('dashboard.html', title="Dashboard | List", user=user, college=college)

@server.route('/dashboard/users', methods=["GET", "POST"])
@login_required
def dashboard_users():
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	data = User.query.filter_by(college_name=current_user.college_name)
	form = RegistrationForm()
	form2 = CategoryForm()
	cat = Category.query.filter_by(college_name=current_user.college_name)
	if form.validate_on_submit():
		category_name = request.form['category_name']
		print(category_name)
		new_user = User(form.contact.data, form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, form.rfid.data, category_name,current_user.college_name)
		dbase.session.add(new_user)
		dbase.session.commit()
		return redirect(url_for('dashboard_users'))

	return render_template('dashboard_users.html', title="Dashboard | Users", cat=cat,form2=form2, form=form,data=data, user=user, college=college)

@server.route('/add/category',methods=["POST"])
@login_required
def add_category():
	form2 = CategoryForm()
	if form2.validate_on_submit():
		new_cat = Category(form2.category_name.data, current_user.college_name)
		dbase.session.add(new_cat)
		dbase.session.commit()
	return redirect(url_for('dashboard_users'))

@server.route('/delete/user/<int:id>', methods=["POST", "GET"])
@login_required
def delete_user(id):
	print('halooooooo')
	del_user = User.query.filter_by(id=id).first()
	print(id)
	print(del_user.username)
	dbase.session.delete(del_user)
	dbase.session.commit()
	return redirect(url_for('dashboard_users'))

@server.route('/dashboard/profile', methods=["GET", "POST"])
@login_required
def dashboard_profile():
	user = current_user
	form = RegistrationForm()
	cat = Category.query.filter_by(college_name=current_user.college_name)
	college = College.query.filter_by(college_name=current_user.college_name).first()
	if form.validate_on_submit():
		category_name = request.form['category_name']
		user.contact = form.contact.data
		user.firstname = form.firstname.data
		user.lastname = form.lastname.data
		user.email = form.email.data
		user.username = form.username.data
		user.user_type = category_name
		dbase.session.commit()
		return redirect(url_for('dashboard_profile'))

	return render_template('dashboard_profile.html', title="Dashboard | Profile",cat=cat,form=form, user=user, college=college)

@server.route('/college', methods=["GET", "POST"])
@login_required
def college():
	form = CollegeForm()
	if form.validate_on_submit():
		new_college = College(form.college_pic.data,form.college_name.data)
		print(form.college_pic.data)
		dbase.session.add(new_college)
		dbase.session.commit()
		update_user = current_user
		print(form.college_name.data)
		update_user.college_name = form.college_name.data
		print(update_user.college_name)
		dbase.session.commit()
		return redirect(url_for('dashboard'))
	return render_template('college.html', title='Add College | InPack', form=form)


@server.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))