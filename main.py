from flask import Flask, jsonify, request,render_template

web_site = Flask(__name__)
data=[]	
@web_site.route("/")
def login():
	return render_template('login.html')

@web_site.route('/index')
def index():
	return render_template('index.html')

@web_site.route("/api/v1.0/send",methods=["POST"])	
def send_test():
	username=request.form["username"]
	return "<h1>text, "+ username+ "!<h1>"

web_site.run(host='0.0.0.0', port=8080)	