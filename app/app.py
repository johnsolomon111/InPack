from app import *
from sqlalchemy import or_
<<<<<<< HEAD
from sqlalchemy import and_
=======
>>>>>>> 248a0241aaa28639311c3dd373413adc69e8dcfc

from flask import render_template, request, redirect, url_for, flash, request
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@server.route('/', methods=["GET","POST"])
def index():
	form = LoginForm()
	if current_user.is_authenticated is True:
<<<<<<< HEAD
		return redirect(url_for('dashboard', page_num=1))
=======
		return redirect(url_for('dashboard'))
>>>>>>> 248a0241aaa28639311c3dd373413adc69e8dcfc
	elif form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.rfid, form.rfid.data):
				login_user(user)
<<<<<<< HEAD
				return redirect(url_for('dashboard', page_num=1))
=======
				return redirect(url_for('dashboard'))
>>>>>>> 248a0241aaa28639311c3dd373413adc69e8dcfc
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
				return redirect(url_for('dashboard', page_num=1))
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

@server.route('/dashboard/<int:page_num>', methods=["GET", "POST"])
@login_required
def dashboard(page_num):
	user = current_user
	form = ItemForm()
	form2 = CategoryForm()
	form3 = BorrowForm()
	form4 = BorrowerForm()
	total_item = Item.query.filter_by(college_name=current_user.college_name)
	total_borrow = BorrowedItem.query.filter_by(college_name=current_user.college_name)
	borrower = Borrower.query.all()
	search_form = SearchForm()
	query = search_form.search.data

	t_data = 0
	t_borrow = 0
	for i in total_borrow:
		t_borrow = t_borrow + i.quantity
	for total in total_item:
		t_data = t_data + total.quantity
	threads = total_item.paginate(per_page=5,page=page_num,error_out=False)
	cat = Category.query.filter_by(college_name=current_user.college_name)
	x = cat.count()
	college = College.query.filter_by(college_name=current_user.college_name).first()
	return render_template('dashboard.html', title="Dashboard | List",query=query, search_form=search_form, x=x,form3=form3,borrower=borrower,form4=form4,threads=threads,t_borrow=t_borrow,t_data=t_data,cat=cat,form=form,form2=form2, user=user, college=college)

@server.route('/add/item', methods=["POST"])
@login_required
def add_item():
	form = ItemForm()
<<<<<<< HEAD
	if form.validate_on_submit():
		category_name = request.form['category_name']
		new_item = Item(form.item_name.data, category_name, form.quantity.data, current_user.college_name, 'Available')
		dbase.session.add(new_item)
		dbase.session.commit()
	return redirect(url_for('dashboard', page_num=1))

@server.route('/borrow/item/<int:id>',methods=["POST","GET"])
@login_required
def borrow_item(id):
	item = Item.query.filter_by(item_id=id).first()
	form3 = BorrowForm()
	borrower = Borrower.query.all()
	form4 = BorrowerForm()


	if item.quantity >= form3.quantity.data:
		
		if form3.validate_on_submit():
			item.quantity = item.quantity - form3.quantity.data
			new_borrow = BorrowedItem(item.item_name, item.item_id, form3.quantity.data, current_user.college_name)
			dbase.session.add(new_borrow)
			dbase.session.commit()  

		if request.method == 'POST':
			borrow_fname  = request.form['borrow_fname']
			borrow_lname = request.form['borrow_lname']
			borrow_idno = request.form['borrow_idno']
			borrow_college = request.form['borrow_college']
			borrow_course = request.form['borrow_course']
			borrow_status = ['Borrowed']
			borrower= Borrower(borrow_fname=borrow_fname, borrow_lname=borrow_lname, borrow_idno=borrow_idno,borrow_college=borrow_college, borrow_course=borrow_course, item_id=item.item_id, quantity=form3.quantity.data)
			dbase.session.add(borrower)
			dbase.session.commit()      
		return redirect(url_for('dashboard', page_num=1))
	return redirect(url_for('dashboard', page_num=1))

@server.route('/view/borrowed_items', methods=["GET", "POST"])
@login_required
def borrowed_items():
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	borrow = Borrower.query.all()
	item = Item.query.all()
	return render_template('viewborrowed.html', item = item, user=user, college=college, borrow=borrow, title='Borrowed Items | InPack')

@server.route('/item/<item_id>', methods=["GET", "POST"])
@login_required
def view_item(item_id):
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	item = Item.query.get_or_404(item_id)
	items = Item.query.filter_by(college_name=current_user.college_name)
	form = ItemForm()
	cat = Category.query.filter_by(college_name=current_user.college_name)


	return render_template('viewitem.html', cat = cat, form = form, items=items, item = item, user=user, college=college, title='Items | InPack')

@server.route('/update/item/<int:item_id>', methods=["GET", "POST"])
@login_required
def update_item(item_id):
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	item = Item.query.get_or_404(item_id)
	items = Item.query.filter_by(college_name=current_user.college_name)
	form = ItemForm()
	cat = Category.query.filter_by(college_name=current_user.college_name)

	if form.validate_on_submit():
		item.item_name = form.item_name.data
		category_name = request.form['category_name']
		item.quantity = form.quantity.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('view_item', item_id=item.item_id))
	return redirect(url_for('view_item', item_id=item.item_id))

@server.route('/delete/item/<int:id>', methods=["POST", "GET"])
@login_required
def delete_item(id):
	del_item = Item.query.filter_by(item_id=id).first()
	dbase.session.delete(del_item)
	dbase.session.commit()
	return redirect(url_for('dashboard', page_num=1))

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
=======
	if form.validate_on_submit():
		category_name = request.form['category_name']
		new_item = Item(form.item_name.data, category_name, form.quantity.data, current_user.college_name, 'Available')
		dbase.session.add(new_item)
		dbase.session.commit()
	return redirect(url_for('dashboard', page_num=1))

@server.route('/borrow/item/<int:id>',methods=["POST","GET"])
@login_required
def borrow_item(id):
	item = Item.query.filter_by(item_id=id).first()
	form3 = BorrowForm()
	borrower = Borrower.query.all()
	form4 = BorrowerForm()


	if item.quantity >= form3.quantity.data:
		
		if form3.validate_on_submit():
			item.quantity = item.quantity - form3.quantity.data
			new_borrow = BorrowedItem(item.item_name, item.item_id, form3.quantity.data, current_user.college_name)
			dbase.session.add(new_borrow)
			dbase.session.commit()	

		if request.method == 'POST':
			borrow_fname  = request.form['borrow_fname']
			borrow_lname = request.form['borrow_lname']
			borrow_idno = request.form['borrow_idno']
			borrow_college = request.form['borrow_college']
			borrow_course = request.form['borrow_course']
			borrow_status = ['Borrowed']
			borrower= Borrower(borrow_fname=borrow_fname, borrow_lname=borrow_lname, borrow_idno=borrow_idno,borrow_college=borrow_college, borrow_course=borrow_course, item_id=item.item_id, quantity=form3.quantity.data)
			dbase.session.add(borrower)
			dbase.session.commit()		
		return redirect(url_for('dashboard', page_num=1))
	return redirect(url_for('dashboard', page_num=1))

@server.route('/view/borrowed_items', methods=["GET", "POST"])
@login_required
def borrowed_items():
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	borrow = Borrower.query.all()
	item = Item.query.all()
	return render_template('viewborrowed.html', item = item, user=user, college=college, borrow=borrow, title='Borrowed Items | InPack')

@server.route('/item/<item_id>', methods=["GET", "POST"])
@login_required
def view_item(item_id):
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	item = Item.query.get_or_404(item_id)
	items = Item.query.filter_by(college_name=current_user.college_name)
	form = ItemForm()
	cat = Category.query.filter_by(college_name=current_user.college_name)


	return render_template('viewitem.html', cat = cat, form = form, items=items, item = item, user=user, college=college, title='Items | InPack')

@server.route('/update/item/<int:item_id>', methods=["GET", "POST"])
@login_required
def update_item(item_id):
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	item = Item.query.get_or_404(item_id)
	items = Item.query.filter_by(college_name=current_user.college_name)
	form = ItemForm()
	cat = Category.query.filter_by(college_name=current_user.college_name)

	if form.validate_on_submit():
		item.item_name = form.item_name.data
		category_name = request.form['category_name']
		item.quantity = form.quantity.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('view_item', item_id=item.item_id))
	return redirect(url_for('view_item', item_id=item.item_id))

@server.route('/delete/item/<int:id>', methods=["POST", "GET"])
@login_required
def delete_item(id):
	del_item = Item.query.filter_by(item_id=id).first()
	dbase.session.delete(del_item)
	dbase.session.commit()
	return redirect(url_for('dashboard', page_num=1))

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
>>>>>>> 248a0241aaa28639311c3dd373413adc69e8dcfc
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
	return redirect(url_for('dashboard', page_num=1))

@server.route('/categories', methods=["GET","POST"])
@login_required
def categories():
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	category = Category.query.all()
	borrow = Borrower.query.all()
	item = Item.query.all()
	form = CategoryForm()

	if form.validate_on_submit():
		category.category_name = form.category_name.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('categories'))
		
	return render_template('categories.html', title = "Categories", form = form, item = item,  category = category, user = user, college = college)
	

@server.route('/categories/update/<int:category_id>', methods=["POST", "GET"])
@login_required
def update_category(category_id):
	user = current_user
	college = College.query.filter_by(college_name=current_user.college_name).first()
	category = Category.query.get_or_404(category_id)
	borrow = Borrower.query.all()
	item = Item.query.all()
	form = CategoryForm()

	if form.validate_on_submit():
		category.category_name = form.category_name.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('categories'))
	return redirect(url_for('categories'))


@server.route('/categories/delete/<int:category_id>', methods=["POST", "GET"])
@login_required
def delete_category(category_id):
	del_category = Category.query.filter_by(category_id=category_id).first()
	dbase.session.delete(del_category)
	dbase.session.commit()
	return redirect(url_for('categories'))

@server.route('/delete/user/<int:id>', methods=["POST", "GET"])
@login_required
def delete_user(id):
	del_user = User.query.filter_by(id=id).first()
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
		user.rfid = form.rfid.data
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
		return redirect(url_for('dashboard', page_num=1))
	return render_template('college.html', title='Add College | InPack', form=form)

@server.route('/search', methods=['GET', 'POST'])
<<<<<<< HEAD
@login_required
def search():
	page_num = 1
	user = current_user
	form = ItemForm()
	form2 = CategoryForm()
	form3 = BorrowForm()
	form4 = BorrowerForm()
	search_form = SearchForm()
	query = search_form.search.data
	borrower = Borrower.query.all()


	if search_form.validate_on_submit():
		total_item = dbase.session.query(Item).filter( ( Item.college_name == current_user.college_name ) & ( Item.item_name.ilike(query) )  )


		total_borrow = BorrowedItem.query.filter_by(college_name=current_user.college_name)
		t_data = 0
		t_borrow = 0



		for i in total_borrow:
			t_borrow = t_borrow + i.quantity
		for total in total_item:
			t_data = t_data + total.quantity
		threads = total_item.paginate(per_page=5,page=page_num,error_out=False)
		cat = Category.query.filter_by(college_name=current_user.college_name)
		x = cat.count()
		college = College.query.filter_by(college_name=current_user.college_name).first()

		return render_template('dashboard.html', title="Dashboard | List",query=query, search_form=search_form, x=x,form3=form3,borrower=borrower,form4=form4,threads=threads,t_borrow=t_borrow,t_data=t_data,cat=cat,form=form,form2=form2, user=user, college=college)    
	return redirect(url_for('dashboard', page_num=1))
=======
def search():
    search_form = SearchForm()
    form = ItemForm()
    query = search_form.search.data
    if search_form.validate_on_submit():
        qry = dbase.session.query(Item).filter(or_( Item.item_name.ilike(query), Item.category.ilike(query) ) )
        items = qry.all()
        return render_template('dashboard.html',form=form, search_form=search_form, query=query, items=items)      
    return redirect(url_for('dashboard'))
>>>>>>> 248a0241aaa28639311c3dd373413adc69e8dcfc


@server.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))