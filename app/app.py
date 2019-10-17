from app import *
from flask import Flask, render_template, url_for, flash, redirect, session
import os 
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
	return render_template('index.html')


@app.route('/landing_page',methods=['GET','POST'])
def landing():
    return render_template('landingpage.html')


if __name__ == '__main__':
	app.run(debug=True)