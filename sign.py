from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256

def sign(m):
    #generate public key
    #Your code here
    priv_key, pub_key = keys.gen_keypair(curve.secp256k1) 
    print(priv_key)
    print(pub_key)
    (r,s) = ecdsa.sign(m,priv_key,secp256k1,hashfunc=sha256)
    print((r,s))
    valid = ecdsa.verify((r,s),m,pub_key, secp256k1)
    print(valid)
    assert isinstance( pub_key, point.Point )
    assert isinstance( r, int )
    assert isinstance( s, int )
    return(pub_key, [r,s])
