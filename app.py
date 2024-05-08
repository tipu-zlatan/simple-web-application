import os
from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

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
#    if request.headers.getlist("X-Forwarded-For"):
#       ip = request.headers.getlist("X-Forwarded-For")[0]
#    else:
#      ip = request.remote_addr
 #   return str(request.headers)
    request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
#    return jsonify({'ip': request.remote_addr}), 200
    return str(request.environ)
   # return str(request.access_route)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, ssl_context='adhoc') #
