import os
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route("/")
def main():
    color = os.environ.get('COLOR', "green") 
    message = "Welcome !!! This is "+color+" environment" 
    return message

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
