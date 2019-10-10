from app import *

from flask import render_template


@server.route('/', methods=["GET"])
def index():
	return render_template('index.html', title="Inpack")

@server.route('/login', methods=["GET"])
def login_with_password():
	return render_template('login.html', title="Log In with Password")