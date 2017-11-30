from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

#def index():
#	return "Hello JLK Inspection"

def login():
	error=None
	if request.method == 'POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			error = 'Try again'
		else:
			return redirect(url_for('secret'))
	return render_template('index.html',error=error)

@app.route('/secret')

def secret():
	return "Secret"



if __name__=="__main__":
	app.run()

