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
        return render_template('dashboard.html', items=items, form=form)
    return render_template('dashboard.html', items=items, form=form, title='Dashboard')
	
@server.route('/item/<int:item_id>', methods=['GET', 'POST'])
def viewitem(item_id):
    items = Item.query.get_or_404(item_id)
    item = Item.query.filter_by(item_id=item_id).all()
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
    return render_template("viewitems.html", items=items, item=item, form=form, title='View Item')

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
    return render_template('categories.html', items=items, title='Dashboard')