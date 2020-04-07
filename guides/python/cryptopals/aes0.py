#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 7

# THIS IS A SCRIPT

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# mylibs
import b64

# opens the file
with open('files/aes-7.txt','r') as f:
    buf = f.read()
    buf = buf.replace('\n','')
    buf = b64.decode(buf)

key = 'YELLOW SUBMARINE'.encode('utf8')
print(key)

# initialize AES cipher in ECB mode
cipher = Cipher( algorithms.AES(key), modes.ECB(), backend = default_backend() )
de = cipher.decryptor()
msg = de.update(buf) + de.finalize()
print(msg.decode('utf8'))
