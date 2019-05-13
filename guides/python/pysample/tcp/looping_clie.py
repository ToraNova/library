#!/usr/bin/python3
import socket
import sys

if __name__ == "__main__":

	if(len(sys.argv) < 2):
		print("Please specify port")
		exit()
	else:
		try:
			portn = int(sys.argv[1])
		except Exception as e:
			print(str(e))
			exit()

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#specify the socket
	server_address = ('localhost', portn)
	print('connecting to %s port %s' % server_address)
	sock.connect(server_address)
	try:
		while True:
			sendmsg = input("Input :")
			print("sending '%s'" % sendmsg)
			sock.sendall(sendmsg.encode('utf-8'))
			try:
				recvmsg = sock.recv(3,0x40) #non blocking
			except BlockingIOError as e:
				print("No msg recv.",str(e))
				recvmsg = None
			if(recvmsg != None):
				recvstr = recvmsg.decode('utf-8')
				print("received '%s'" % recvstr)
	finally:
		print('closing socket')
		sock.close()
