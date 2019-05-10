#!/usr/bin/python3

import socket
import sys
from pkg import timer, fileman

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)


# Listen for incoming connections
if __name__ == "__main__":
	print('starting up on %s port %s' % server_address)
	sock.bind(server_address)
	sock.listen(1) #listen for one
	t = timer.ToraTime(0)
	while True:
		# Wait for a connection
		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
			print('connection from', client_address)
			data = connection.recv(16)
			if(fileman.checkFiles('t.run','flags')):
				pass #ignore everything
			else:
				if data:
					data = data.decode('utf-8')
					print(data)
					if( data == "ignore me"):
						print("Starting Ignore")
						t = timer.ToraTime(10000,False)
						t.start()
		    
		finally:
			# Clean up the connection
			connection.close()

