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