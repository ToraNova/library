#!/usr/bin/python3

from flask import Flask
from flask import request
from flask_basicauth import BasicAuth

app = Flask(__name__)

# DOING BASIC AUTH IN HTTP (INSECURE) IS POINTLESS
# AS ATTACKERS CAN SNIFF THE PASSWORD OFF THE NETWORK
# PLEASE DO THIS ONLY IN SECURED CONNECTIONS (SSL/TLS)
app.config['BASIC_AUTH_USERNAME'] = "admin"
app.config['BASIC_AUTH_PASSWORD'] = "Admin123"
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

def printSep():
    for i in range(99):
        print('-',end='')
    print('-')

@app.route('/', methods=['GET','POST'])
@basic_auth.required
def msgRepeat():
    print(request.authorization)
    return '200,ok'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9000)



