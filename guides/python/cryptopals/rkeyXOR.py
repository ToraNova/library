#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 5

from lkupmap import hexlkup, hexmap
from hexutf8 import hex2utf8_literal, utf82hex_literal

'''
repeating-byte XOR with literal char
b can be [0x0a,0x0b] OR 'abc'
smth like a vigenere cipher
'''
def repeatxor_literal(s, k):

    # assume k could be 'abc' or smth like that
    # convert it to list
    if type(k) == str:
        tmp = []
        for c in k:
            tmp.append(ord(c))
        k = tmp
        del tmp

    # ensure correct type
    if type(k) == list and len(k) > 0:
        pass
    else:
        return f'invalid key type {type(k)}, must be non empty list or str'

    # assume k is [0x0a,0x0b,0x10] or smth like that
    if(type(k[0]) != int):
        return f'invalid element in key {type(k[0])}, must be int'

    #split key into high/low nibble
    kh = []
    kl = []
    for e in k:
        kh.append((e & 0xf0) >> 4)
        kl.append(e & 0x0f)

    kptr = 0 # key pointer, rotates from 0 to len(k)
    idx = 0
    out = ''
    # keep encrypting until we run out
    while idx < len(s):
        th = hexlkup[ hexmap[ s[idx] ] ^ kh[kptr] ]
        tl = hexlkup[ hexmap[ s[idx+1] ] ^ kl[kptr] ]
        kptr = (kptr + 1) % len(k) # rotate
        idx = idx + 2
        out = out + th + tl
    return out

if __name__ == '__main__':
    plain = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    key = 'ICE'
    res = utf82hex_literal(plain)
    print(res)
    res = repeatxor_literal(res,key)
    print(res)

