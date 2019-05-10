#!/usr/bin/python3

# random key generation routine
# used as a tool for testing
# Key generation

import base64
import os
import sys
import binascii

BLOCK_SIZE=32

if __name__ == "__main__":
	
	block_size = None

	if(len(sys.argv) < 2):
		print("Please specify a blocksize i.e no. of bytes")
		print("randkeygen <block_size:int>")
		exit(1)

	try:
		block_size = int(sys.argv[1])
	except Exception as e:
		print("Please specify blocksize as int only !",str(e))
		exit(1)

	#input sanitized (partially)

	genkey = os.urandom(block_size)
	print("{} byte random key :".format(block_size))
	print("Base64	: ",base64.b64encode(genkey).decode('utf-8'))
	print("Hex	: ",' '.join("{:02X}".format(b) for b in genkey ))
	


