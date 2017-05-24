#_*_coding:utf-8_*_
from flask import Flask,url_for
app=Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello,World!"

@app.route("/hello")
def hello():
	return "GGSIMIDA"


@app.route('/user/<username>')
def show_user_profile(username):
	return 'User names is: %s'% username


@app.route('/post/<int:post_id>')

def show_post(post_id):
	return "Post id is %d"%post_id

"""
 Accessing it without a trailing slash will
 cause Flask to redirect to the canonical URL with the trailing slash.
"""
@app.route('/projects/')
def show_project():
	return "My projects"



"""
The URL is defined without a trailing slash
Accessing the URL with a trailing slash will produce a 404 “Not Found” error.
"""
@app.route('/about')
def show_about():
	return "My About"

with app.test_request_context():
	url_for('static',filename='gg.html')

