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
	if form.validate_on_submit():
		new_user = User(form.contact.data, form.firstname.data, form.lastname.data, form.email.data, form.username.data, form.password.data, form.rfid.data)
		dbase.session.add(new_user)
		dbase.session.commit()

		user = User.query.filter_by(username=form.username.data).first()
		login_user(user)
		return redirect(url_for('dashboard'))
	return render_template('signup.html', title="Get Started!", form=form)

@server.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
	items =  Item.query.all()
	return render_template('dashboard.html', title="Dashboard")

@server.route('/categories', methods=["GET", "POST"])
def categories():
    items =  Item.query.all()
    form = ItemForm()
    if request.method== 'POST':
        category = request.form['category']
        item = Item(category=category)

    return render_template('categories.html', form=form,title="Categories")	

@server.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@server.route('/items', methods=["GET", "POST"])
def items():
    items =  Item.query.all()
    form = ItemForm()
    if request.method == 'POST':
        item_name  = request.form['item_name']
        category = request.form['category']
        status = request.form['status']
        quantity = request.form['quantity']
        tag = request.form['tag']

        item = Item(item_name=item_name, category=category, status=status, quantity=quantity, tag=tag)
        dbase.session.add(item)
        dbase.session.commit()
        items = Item.query.all()
        return render_template('items.html', items=items, form=form)
    return render_template('items.html', items=items, form=form, title='Items')
    
	
@server.route('/item/<int:item_id>', methods=['GET', 'POST'])
def viewitem(item_id):
    items = Item.query.get_or_404(item_id)
    item = Item.query.filter_by(item_id=item_id).all()
    form_update = ItemForm()      
    borrow = BorrowItem.query.all()
    form = BorrowForm()
    if form_update.validate_on_submit():
        items.item_name = form_update.item_name.data
        items.category = form_update.category.data
        items.status = form_update.status.data
        items.quantity = form_update.quantity.data
        items.tag = form_update.tag.data
        dbase.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('viewitem', item_id=items.item_id))
    elif request.method == 'GET':
        form_update.item_name.data = items.item_name
        form_update.category.data = items.category
        form_update.status.data = items.status
        form_update.quantity.data = items.quantity
        form_update.tag.data = items.tag

    if request.method == 'POST':
        borrow_fname  = request.form['borrow_fname']
        borrow_lname = request.form['borrow_lname']
        borrow_idno = request.form['borrow_idno']
        borrow_college = request.form['borrow_college']
        borrow_course = request.form['borrow_course']
        borrow_status = request.form['borrow_status']
        borrowitem = BorrowItem(borrow_fname=borrow_fname, borrow_lname=borrow_lname, borrow_idno=borrow_idno,borrow_college=borrow_college, borrow_course=borrow_course, borrow_status=borrow_status, item_id=item_id)
      
        dbase.session.add(borrowitem)
        dbase.session.commit()
        borrow = BorrowItem.query.all()
        return render_template('viewborrowed.html', borrow=borrow, items=items, form=form, form_update=form_update)
    return render_template("viewitems.html", items=items, item=item, form=form, form_update=form_update, title='View Item')

@server.route("/item/<int:item_id>/delete", methods=['POST'])
def deleteitem(item_id):
    items = Item.query.get_or_404(item_id)
    dbase.session.delete(items)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('dashboard'))	

@server.route('/borroweditems', methods=["GET","POST"])
def viewborroweditems():
    borrow = BorrowItem.query.all()
    items =  Item.query.all()
    return render_template('viewborrowed.html', items=items, borrow=borrow, title='Borrowed Items')	