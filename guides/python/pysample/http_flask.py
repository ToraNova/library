#!/usr/bin/python3

from flask import Flask
from flask import request

app = Flask(__name__)

def printSep():
	for i in range(99):
		print('-',end='')
	print('-')

@app.route('/', methods=['GET','POST'])
def msgRepeat():
	printSep()
	print("Incoming",request.method,"request...\n")
	print("HEADERS :")
	print(request.headers)

	#print("ARGS :")
	#print(request.args)

	print("FORM :")
	print(request.form)
	
	#print("VALUES :")
	#print(request.values)
	
	print("COOKIES :")
	print(request.cookies)

	print("DATA :")
	print(request.data)
	printSep()
	return '200,ok'

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=8000)



