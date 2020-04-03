#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 5

from lkupmap import hexlkup, hexmap
from hexutf8 import hex2utf8_literal, utf82hex_literal
from sbyteXOR import sbxbreak_english
from hexb64 import b642hex_literal
import base64

'''
repeating-byte XOR with literal char
b can be [0x0a,0x0b] OR 'abc' OR b'abc'
smth like a vigenere cipher
'''
def repeatxor_literal(s, k):

    if(type(s) != str):
        return f'repeatxor literal cannot be used with type \'{type(S)}\''

    # assume k could be 'abc' or smth like that
    # convert it to list
    if type(k) == str:
        tmp = []
        for c in k:
            tmp.append(ord(c))
        k = tmp
        del tmp
    elif type(k) == bytes:
        k = [ c for c in k]

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

'''
computes hamming weight of an int
if a = 0x0f, hamming weight is 4
hamming weight is how many bits is set
'''
def hamweight(a):
    out = 0
    while a > 0:
        out = out + 1 if a & 0x1 > 0 else out
        a = a >> 1
    return out

'''
compute edit distance, the number of bits
required to change a->b or vice versa
'''
def editdist(a, b):
    # compute edit distance between two string
    # for every difference in char length, is is 8 bits or a byte
    if(type(a) != type(b)):
        return None
    out = len(a) - len(b) if len(a) > len(b) else len(b) - len(a)
    out = out*8
    ml = len(b) if len(a) > len(b) else len(a)
    if(type(a) == bytes):
        for i in range(0,ml):
            out = out + hamweight( a[i] ^ b[i] )
    elif(type(a) == str):
        for i in range(0,ml):
            # xorring gives diff, just need to find out how many 1's in result
            out = out + hamweight( ord(a[i]) ^ ord(b[i]) )
    else:
        return None
    return out

if __name__ == '__main__':
    #plain = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    #key = 'ICE'
    #res = utf82hex_literal(plain)
    #print(res)
    #res = repeatxor_literal(res,key)
    #print(res)

    #a = 'this is a test'
    #b = 'wokka wokka!!!'
    #c = 0x0f
    #print(hamweight(c))
    #print( editdist(a,b))

    with open("rhex-6.txt","r") as f:
        buf = f.read()
        buf = buf.replace('\n','') #removes newlines
        buf = base64.b64decode(buf)

    stat_ks = {}
    for klen in range(2,50):
        s1 = buf[ 0: klen ] # first klen bytes
        s2 = buf[ klen: 2*klen] # klen bytes after first klen bytes
        stat_ks[klen] = editdist(s1,s2)

    for cnt, ks in enumerate(sorted(stat_ks, key=stat_ks.get)):
        print(ks,stat_ks[ks])
        if(cnt > 10):
            break

    # we guess this is the keylength
    klen = sorted(stat_ks, key=stat_ks.get)[0]
    hist = {}
    for i in range(klen):
        hist[i] = bytes( buf[j] for j in range(i,len(buf),klen)  )

    key = []
    for k,i in hist.items():
        for res in sbxbreak_english(i, 10):
            key.append(res[0])

    #with open("rhex-6.txt","r") as f:
    #    buf = f.read()
    #    buf = buf.replace('\n','') #removes newlines
    #    buf = b642hex_literal(buf)
    #res = repeatxor_literal(buf,key)
    #res = hex2utf8_literal(res)
    #print(res)

