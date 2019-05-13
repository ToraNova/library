#!/usr/bin/python3

import socket
import sys
import subprocess


# Bind the socket to the port
server_address = ('localhost', 10000)

# Listen for incoming connections
if __name__ == "__main__":
	print('starting up on %s port %s' % server_address)
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP socket
		sock.bind(server_address)
		sock.listen(1) #listen for one
		while True:
			try:
				print('waiting for a connection') # Wait for a connection
				connection, client_address = sock.accept()
				print('connection from', client_address)
				data = connection.recv(16) # Receive the data in small chunks and retransmit it
				connection.sendall(data)
				data = data.decode("utf-8")
				#processing is done here
				childproc = subprocess.Popen(['./child.py',data],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				out,err = childproc.communicate(timeout=5)
				print("STDOUT:",out,"/ STDERR:",err)
			except Exception as e:
				print("Exception has occurred:",str(e))
				out,err = childproc.communicate()
				print("STDOUT:",out,"/ STDERR:",err)
			finally:
				# Clean up the connection
				connection.close()
	finally:
		sock.close() #shutdowns and deallocate the socket
