from flask import Flask,request

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index(name):
	return "This is me here"