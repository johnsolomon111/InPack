from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

server = Flask(__name__)
dbase = SQLAlchemy(server)

server.config['SECRET_KEY'] = 'secretsecretsecret'
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/inpack'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(server)

from app.models import *
from app.forms import *
from app.app import *

dbase.create_all()