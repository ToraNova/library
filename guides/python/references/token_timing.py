# tokenization testing script
# extracted from Jason Loh's JT lib

from pypbc import *
import os, sys, time
from Crypto.Cipher import AES
import hashlib
import numpy

def hexxor(a, b):    # xor two hex strings of the same length
	return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(a, b)])

if __name__ == "__main__":

	# file reading for generator and sys params
	params_file = open("SystemParams.txt", "r")
	stored_params = params_file.read()
	params = Parameters(param_string = stored_params)
	params_file.close()

	keys_file = open("JT2_Keys.txt", "r")
	pairing = Pairing(params)
	g = Element(pairing, G2, value = keys_file.readline())
	pk_rg = Element(pairing, G2, value = keys_file.readline())
	keys_file.close()

	B = g ** 2

	k = os.urandom(16)
	converted_key = Element.from_hash(pairing, Zr, k)
	
	time0 = []
	time1 = []
	
	runinstance = 3000
	

	Ecipher = AES.new( k, AES.MODE_ECB)
	for i in range(runinstance):
		startime = time.time()
		
		t = os.urandom(16)
		s0 = os.urandom(16)
		
		enc0 = Ecipher.encrypt( t )
		
		Ecipher0 = AES.new( enc0, AES.MODE_ECB)
		enc1 = Ecipher0.encrypt( s0 )

		endtime = time.time() - startime
		time1.append(endtime)
	
	tmp = numpy.average(time1)
	print("%.10f" % tmp )
	
	for i in range(runinstance):
		startime = time.time()
		#-------------------------------------------------
		t = os.urandom(16)
		s0 = os.urandom(16)
		#s1 = bytes([(int(s0[0]) +1)]) + s0[1:]
		
		#print(s0)
		#print(s1)

		hashed_token = Element.from_hash(pairing, Zr, t)
		
		C = g ** hashed_token
		D = B ** -1
		C = (C * D) ** converted_key
		C = hashlib.sha256(str(C).encode('utf-8')).hexdigest()
		C = hexxor(C[:32], C[-32:])

		Ecipher = AES.new( C, AES.MODE_ECB)
		enc0 = Ecipher.encrypt( s0 )
		#enc1 = Ecipher.encrypt( s1 )
		#print(enc1)
		# AES 16 byte block with A as key
		#Ecipher = AES.new( A, AES.MODE_ECB)	
		#------------------------------------------------
		endtime = time.time() - startime
		
		time0.append( endtime )
 
	tmp2 = numpy.average(time0)

	print("%.10f" % tmp2)
	print("Factor %f" % (float(tmp2)/float(tmp)))
		

