from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def Index():
	user = {'nickname':'BigO'}
	return render_template('index.html',titile='Home',user=user)

