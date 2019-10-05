#!/usr/bin/python3

# used to encrypt a byte string
# used as a tool for testing
# AES encryption

from Crypto.Cipher import AES
import base64
import os
import sys
import binascii

def rawpad(s,BLOCK_SIZE):
	#pad it with the characters representing original block size length
        return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def rawunpad(s):
	#unpad by reading original blocksize length, and stripping the pad away
	return s[:-ord(s[len(s)-1:])]

def gethex_bstring(s):
	#get the hex representation of a byte string (as a string)
	return ''.join("{:02X}".format(b) for b in s )

def gethex_sstring(s):
	#get the hex representation of a string (as a string)
	return ''.join("{:02X}".format(ord(b)) for b in s )


if __name__ == "__main__":

	e_key = None
	plain = None
	allz = False

	AES_mode = AES.MODE_CBC

	#input parsing
	if(len(sys.argv) < 3):
		print("Please specify key and msg")
		print("aes_enc <key:base64 16bytes> <msg> <flag>")
		print("b flag to use ECB mode")
		print("c flag to use CTR mode")
		print("p flag to encrypt ONLY 15bytes of the message (used with ECB)")
		print("default mode is CBC")
		print("flags are appended together, i.e : zb")
		exit(1)

	try:
		e_key = base64.b64decode(sys.argv[1])
		plain = sys.argv[2]
	except Exception as e:
		print("Please specify key as base64 input !",str(e))
		exit(1)

	#additionaly flag parsing
	if(len(sys.argv) > 3):
		if('b' in sys.argv[3]):
			AES_mode = AES.MODE_ECB
		if('p' in sys.argv[3] and len(plain)>15 ):
			plain = plain[:15]
		if('c' in sys.argv[3]):
			AES_mode = AES.MODE_CTR

	#input sanitized (partially)

	padded = rawpad( plain , AES.block_size) 	# input padding, AES block size is fixed to 16 bytes
	iv = os.urandom( AES.block_size ) 		# initialization vector

	print("Encrypting {} ({} bytes) with key 0x{}".format(plain,len(plain),gethex_bstring(e_key)))
	print("Padded Base64		:",base64.b64encode(padded.encode('utf-8')).decode('utf-8'))
	print("Padded Hex		:",gethex_sstring(padded))
	print("Post padding length 	: {} bytes".format(len(padded)))

	if(AES_mode == AES.MODE_ECB):
		Ecipher = AES.new( e_key, AES.MODE_ECB)		# ECB mode does not use IV
	else:
		Ecipher = AES.new( e_key, AES_mode, iv)		# encrypting cipher obj

	block = Ecipher.encrypt(padded)
	cipher = iv + block 				# append the block behind the iv

	print("\nPure cipherblock output")
	print("Base64	:",base64.b64encode(block).decode('utf-8'))
	print("Hex	:",gethex_bstring(block))
	print("Length	: {} bytes".format(len(block)))

	print("\nCiphertext with IV inserted:")
	print("Base64	:",base64.b64encode(cipher).decode('utf-8'))
	print("Hex	:",gethex_bstring(cipher))
	print("Length 	: {} bytes".format(len(cipher)))

	# Decryption checking
	print("\nDecryption checkback...")
	# extract the iv out
	iv = cipher[:AES.block_size]
	cipher = cipher[AES.block_size:]

	if(AES_mode == AES.MODE_ECB):
		Dcipher = AES.new( e_key, AES.MODE_ECB)
	else:
		Dcipher = AES.new( e_key, AES_mode, iv)
	plain = Dcipher.decrypt(cipher)
	plain = rawunpad(plain)
	print("Decrypted plaintext :",plain.decode('utf-8')," Length : {} bytes".format(len(plain)))


