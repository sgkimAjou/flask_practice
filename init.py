from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
	return "Hello JLK Inspection"


if __name__=="__main__":
	app.run()

