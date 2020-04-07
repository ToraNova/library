#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 8

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# mylibs
import b64
from chex import hex2b, b2hex
from rkeyXOR import editdist

if __name__ == "__main__":
    # opens the file
    with open('files/ecb-8.txt','r') as f:
        stat = {}
        key = os.urandom(16)

        ## initialize AES cipher in ECB mode
        ecb = Cipher( algorithms.AES(key), modes.ECB(), backend = default_backend() )

        for idx,line in enumerate(f):
            line = line.strip('\n')
            line = hex2b(line)

            # break line into 16 byte blocks
            blocks = [ line[i:i+16] for i in range(0,len(line),16) ]

            count = 0
            for b in blocks:
                for c in blocks:
                    if c == b:
                        count += 1
                count -= 1

            stat[idx] = count

        for k in sorted(stat, key=stat.get, reverse=True)[:10]:
            print(k, stat[k])
