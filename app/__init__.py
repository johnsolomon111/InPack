from flask import Flask

server = Flask(__name__)

server.config['SECRET_KEY'] = 'secretsecretsecret'


from app.app import *