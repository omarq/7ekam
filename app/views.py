from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def Index():
	user = {'nickname':'BigO'}
	posts =[
	{
		'author':{'nickname':'BigO'},
		'body': 'Beautiful in Rio'

	},
	{
		'author':{'nickname':'Ali'},
		'body':'The Avangers movie was cool !'
	}
	]
	return render_template('index.html',title='Home',user=user,posts=posts)

