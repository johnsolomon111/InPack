from app import dbase, generate_password_hash, UserMixin


class User(UserMixin, dbase.Model):
	__tablename__ = 'user'
	id = dbase.Column(dbase.Integer, primary_key=True)
	contact = dbase.Column(dbase.String(15), nullable=False)
	firstname = dbase.Column(dbase.String(50), nullable=False)
	lastname = dbase.Column(dbase.String(50), nullable=False)
	email = dbase.Column(dbase.String(50), nullable=False)
	username = dbase.Column(dbase.String(50), nullable=False)
	password = dbase.Column(dbase.String(200), nullable=False)
	rfid = dbase.Column(dbase.String(200), nullable=False)

	def __init__(self, contact='', firstname='',lastname='', email='', username='', password='',  rfid=''):
		self.contact = contact
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.username = username
		self.password = generate_password_hash(password, method='sha256')
		self.rfid = generate_password_hash(rfid, method='sha256')

class Item(dbase.Model):
    __tablename__ = "items"

    item_id = dbase.Column(dbase.Integer, primary_key=True)
    item_name = dbase.Column(dbase.String(50))
    category = dbase.Column(dbase.String(50))
    status = dbase.Column(dbase.String(50))
    quantity = dbase.Column(dbase.Integer)

    def __init__(self, item_name='', status='',category='', quantity=''):
        self.item_name = item_name
        self.status = status
        self.category = category
        self.quantity = quantity