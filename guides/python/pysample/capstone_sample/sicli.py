#!/usr/bin/python3
import socket
import sys

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)

if __name__ == "__main__":
	print('connecting to %s port %s' % server_address)
	while True:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(server_address)
		try:
			# Send data
			message = input("Input message:")
			print('sending "%s"' % message)
			sock.sendall(message.encode('utf-8'))

		finally:
			print('closing socket')
			sock.close()
