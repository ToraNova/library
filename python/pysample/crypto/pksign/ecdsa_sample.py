#
#	ECDSA sample signature
# 	for garbling verification
#	https://jhuisi.github.io/charm/

from charm.toolbox.eccurve import prime192v2
from charm.toolbox.ecgroup import ECGroup,ZR,G
from charm.toolbox.PKSig import PKSig

from charm.schemes.pksig.pksig_ecdsa import ECDSA

if __name__ == "__main__":

	# creating an elliptic curve group
	group = ECGroup(prime192v2)
	ecdsa = ECDSA(group)

	# keygen
	(public_key, secret_key) = ecdsa.keygen(0)

	# sign
	msg = "hello world! this is a test message."
	signature = ecdsa.sign(public_key, secret_key, msg)
	v = ecdsa.verify(public_key, signature, msg)
	print( v )
