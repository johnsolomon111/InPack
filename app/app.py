from app import *
from flask import Flask, render_template, url_for, flash, redirect, session
import os 
from flask import render_template
from flask import Flask



@server.route('/', methods=["GET","POST"])
def index():
	return render_template('index.html')


@server.route('/landing_page',methods=['GET','POST'])
def landing():
    return render_template('landingpage.html')


@server.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html')


if __name__ == '__main__':
	server.run(debug=True)