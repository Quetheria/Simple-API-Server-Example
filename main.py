from flask import Flask, jsonify, request,render_template

web_site = Flask(__name__)

@web_site.route('/', methods=["GET"])
def index():
	return render_template('index.html')
@web_site.route('/about')

def about():
	return render_template('about.html')

web_site.run(host='0.0.0.0', port=8080)