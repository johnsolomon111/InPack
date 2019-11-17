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
	college_name = dbase.Column(dbase.String)
	user_type = dbase.Column(dbase.String)
	
	def __init__(self, contact='', firstname='',lastname='', email='', username='', password='',  rfid='', user_type='', college_name=''):
		self.contact = contact
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.username = username
		self.password = generate_password_hash(password, method='sha256')
		self.rfid = generate_password_hash(rfid, method='sha256')
		self.college_name = college_name
		self.user_type = user_type
		
class Item(dbase.Model):
    __tablename__ = "items"

    item_id = dbase.Column(dbase.Integer, primary_key=True)
    item_name = dbase.Column(dbase.String(50))
    category = dbase.Column(dbase.String(50))
    status = dbase.Column(dbase.String(50))
    quantity = dbase.Column(dbase.Integer)
    item_pic = dbase.Column(dbase.String(200))
    college_id = dbase.Column(dbase.String(200))

    def __init__(self, item_name='', status='',category='', quantity='', item_pic='', college_name=''):
        self.item_name = item_name
        self.status = status
        self.category = category
        self.quantity = quantity
        self.item_pic = item_pic
        self.college_name = college_name

class College(dbase.Model):
	__tablename__ = "college"

	college_id = dbase.Column(dbase.Integer, primary_key=True)
	college_name = dbase.Column(dbase.String(200), nullable=False)
	college_pic = dbase.Column(dbase.String(200), nullable=False)

	def __init__(self, college_pic='', college_name=''):
		self.college_name = college_name
		self.college_pic = college_pic

class Category(dbase.Model):
	__tablename__="category"

	category_id = dbase.Column(dbase.Integer, primary_key=True)
	category_name = dbase.Column(dbase.String(100))
	college_name = dbase.Column(dbase.String(200))

	def __init__(self, category_name='', college_name=''):
		self.category_name = category_name
		self.college_name = college_name
