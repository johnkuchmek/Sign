from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):
	#generate public key
	#Your code here
	priv_key, public_key = keys.gen_keypair(curve.secp256k1)
  
	sig= ecdsa.sign(m, priv_key)
  	r = sig[0]
 	s = sig[1]
	assert isinstance( public_key, point.Point )
	assert isinstance( r, int )
	assert isinstance( s, int )
	return( public_key, [r,s] )
