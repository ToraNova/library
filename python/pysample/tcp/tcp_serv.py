#!/usr/bin/python3

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)


# Listen for incoming connections
if __name__ == "__main__":
	print('starting up on %s port %s' % server_address)
	sock.bind(server_address)
	sock.listen(1) #listen for one
	while True:
		# Wait for a connection
		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
			print('connection from', client_address)

			# Receive the data in small chunks and retransmit it
			while True:
				data = connection.recv(16)
				print('received "%s"' % data)
				if data:
					print('sending data back to the client')
					connection.sendall(data)
				else:
					print('no more data from', client_address)
					break
		    
		finally:
			# Clean up the connection
			connection.close()

