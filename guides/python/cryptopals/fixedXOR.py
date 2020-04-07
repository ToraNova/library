#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 2

from chex import hex2b, b2hex
'''
perform XOR of bytes a and b
fast RUN, DOES NOT compare or check
'''
def ffixedXOR(a,b):
    return bytes( [ ca ^ cb for ca,cb in zip(a,b) ] )

'''
perform XOR, check if types are correct
and do truncation/trimming if necessary
'''
def fixedXOR(a,b):
    if type(a) != bytes or type(b) != bytes:
        return f'invalid types \'{type(a)}\' \'{type(b)}\''

    # trimming, i.e
    # a     b
    # 0123  FF
    # 23 XOR FF, 01 trimmed
    if len(a) > len(b):
        d = len(a) - len(b)
        a = a[d:] #cut off the front
    elif len(b) > len(a):
        d = len(b) - len(a)
        b = b[d:] #cut off the front

    return ffixedXOR(a,b)

if __name__ == '__main__':
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'

    a = hex2b(a)
    b = hex2b(b)
    res = ffixedXOR(a,b)
    print( res )

    a = '1c0111001f010100061a024b53535009181c'
    b = '74207468652062756c6c277320657965'
    a = hex2b(a)
    b = hex2b(b)
    res = fixedXOR(a,b)
    print(res)
