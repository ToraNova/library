#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 2

from lkupmap import hexlkup, hexmap

'''
XOR hexstring a with b
'''
def hexxor_literal(a, b):
    # a XOR b = out
    if(len(a) != len(b)):
        return f'xor-ing two elements of unequal length {len(a)} {len(b)}'

    out = ''
    for ca,cb in zip(a,b):
        t = hexlkup[ hexmap[ca] ^ hexmap[cb] ]
        out = out + t
    return out

if __name__ == '__main__':
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'
    res = hexxor_literal(a,b)
    print(res)
