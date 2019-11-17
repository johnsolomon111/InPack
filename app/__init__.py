from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user

server = Flask(__name__)
dbase = SQLAlchemy(server)

server.config['SECRET_KEY'] = 'secretsecretsecret'
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/dbase'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(server)

from app.models import *
from app.forms import *
from app.app import *

dbase.create_all()