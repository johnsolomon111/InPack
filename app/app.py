from app import *

from flask import render_template, request, redirect, url_for, flash
from .models import *
from .forms import *

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
    items =  Item.query.all()
    return render_template('dashboard.html', items=items, title='Dashboard')

@server.route('/items', methods=["GET", "POST"])
def items():
    items =  Item.query.all()
    form = ItemForm()
    if request.method == 'POST':
        item_name  = request.form['item_name']
        category = request.form['category']
        status = request.form['status']
        quantity = request.form['quantity']

        item = Item(item_name=item_name, category=category, status=status,quantity=quantity)
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
        dbase.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('viewitem', item_id=items.item_id))
    elif request.method == 'GET':
        form_update.item_name.data = items.item_name
        form_update.category.data = items.category
        form_update.status.data = items.status
        form_update.quantity.data = items.quantity

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

@server.route('/item/<int:item_id>/update', methods=['GET','POST'])
def updateitem(item_id):
    items = Item.query.get_or_404(item_id)
    form = ItemForm()
    if form.validate_on_submit():
        items.item_name = form.item_name.data
        items.category = form.category.data
        items.status = form.status.data
        items.quantity = form.quantity.data
        dbase.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('viewitem', item_id=items.item_id))
    elif request.method == 'GET':
        form.item_name.data = items.item_name
        form.category.data = items.category
        form.status.data = items.status
        form.quantity.data = items.quantity
    return render_template('updateitems.html', title='Update Item',
                            form=form, items=items)

@server.route("/item/<int:item_id>/delete", methods=['POST'])
def deleteitem(item_id):
    items = Item.query.get_or_404(item_id)
    dbase.session.delete(items)
    dbase.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('dashboard'))

@server.route('/categories', methods=["GET", "POST"])
def categories():
    items =  Item.query.all()
    return render_template('categories.html', items=items, title='Categories')

@server.route('/borroweditems', methods=["GET","POST"])
def viewborroweditems():
    borrow = BorrowItem.query.all()
    items =  Item.query.all()
    return render_template('viewborrowed.html', items=items, borrow=borrow, title='Borrowed Items')