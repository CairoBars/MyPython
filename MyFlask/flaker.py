import os
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash


''''
Flask 提供了两种环境（Context）：应用环境（Application Context）和请求环境（Request Context）。
暂且你所需了解的是，不同环境有不同的特殊变量。例如 request 变量与当前请求的请求对象有关， 
而 g 是与当前应用环境有关的通用变量。我们在之后会深入了解它们。
''''


''''
应用环境在每次请求传入时创建。这里我们并没有请求，所以我们需要手动创建一个应用环境。 
g 在应用环境外无法获知它属于哪个应用，因为可能会有多个应用同时存在。
with app.app_context() 语句为我们建立了应用环境。在 with 语句的内部，
 g 对象会与 app 关联。在语句的结束处，会释放这个关联兵执行所有销毁函数。
 这意味着数据库连接在提交后断开。
''''
def connect_db():
	"""Connects to the specific database"""
	rv=sqlite3.connect(app.config['DATABASE'])
	rv.row_factory=sqlite3.row
	return rv

def init_db():
	with app.app_context():
		db=get_db()
		with app.open_resource('schema.sql',mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def get_db():
	"""Opens a new database connection if there is none yet for the current application context"""
	if not hasattr(g,'sqlite_db'):
		g.sqlite_db=connect_db()
	return g.sqlite_db


""" Flask 提供了 teardown_appcontext() 装饰器。它将在每次应用环境销毁时执行:"""
@app.teardown_appcontext
	"""Close the database again at the end of the request."""
	if hasattr(g,'sqlite_db'):
		g.sqlite_db.close()

if __name__=='__main__':
	app.run()

