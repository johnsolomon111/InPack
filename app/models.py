from app import dbase

class User(dbase.Model):
	__tablename__ = 'user'
	user_id = dbase.Column(dbase.Integer, primary_key=True)
	contact = dbase.Column(dbase.String(15), nullable=False)
	firstname = dbase.Column(dbase.String(50), nullable=False)
	lastname = dbase.Column(dbase.String(50), nullable=False)
	email = dbase.Column(dbase.String(50), nullable=False)
	username = dbase.Column(dbase.String(50), nullable=False)
	password = dbase.Column(dbase.String(50), nullable=False)
	rfid = dbase.Column(dbase.String(50), nullable=False)

	def __init__(self, contact='', firstname='',lastname='', email='', username='', password='',  rfid=''):
		self.contact = contact
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.username = username
		self.password = password
		self.rfid = rfid