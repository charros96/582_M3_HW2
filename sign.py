from fastecdsa.curve import secp256k1
from fastecdsa.keys import export_key, gen_keypair

from fastecdsa import curve, ecdsa, keys, point
from hashlib import sha256
import random

def sign(m):
  
	#generate public key
  keys = gen_keypair(secp256k1)
	#Your code here
  
  #print(keys)
	#public_key = None
  #k = random nonce
  G = secp256k1.G
  n = secp256k1.q
  #k = random.randint(1,n)
  #d = secret key (signing key) random between 1 and order(G)
  d = keys[0]
  #n = order(G)
  #Q = public/verification key = dG
  public_key = keys[1]
  # x1, y1 = kG
  #kG = k*G
	#generate signature
	#Your code here
  # r = x1 mod n
  msg = ecdsa.sign(m,d,secp256k1)
  #s = k_inverse(z+rd) mod n
  r = msg[0]
  #z = hash(m)
  #z = sha256()
  #z = z.update(m)
  #s = pow((z+r*d)/k,1,n)
  s = msg[1]

  assert isinstance( public_key, point.Point )
  assert isinstance( r, int )
  assert isinstance( s, int )
  return( public_key, [r,s] )


