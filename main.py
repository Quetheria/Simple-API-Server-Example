from flask import Flask, jsonify

server = Flask(__name__)

data = {
  "message": "hello, world!"
}

@server.route('/')
def index():
	return jsonify(data)

server.run(host='0.0.0.0', port=8080)