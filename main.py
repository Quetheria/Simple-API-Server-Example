from flask import Flask, jsonify, request,render_template

web_site = Flask(__name__)
usernames=[]
messages=[]	
@web_site.route("/")
def login():
	return render_template('login.html')

@web_site.route("/api/v1.0/send",methods=["POST"])	
def send_test():
	username=request.form["username"]
	return "<h1>text, "+ username+ "!<h1>"
	usernames.append(username)

@web_site.route('/index',methods=["POST"])
def index():
	names=request.form["username"]
	message=request.form["text"]
	usernames.append(names)
	text.append(message)
	return render_template('index.html',names=usernames)



web_site.run(host='0.0.0.0', port=8080)	