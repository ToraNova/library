#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 5

from chex import hex2b, b2hex
from sbyteXOR import sbxbreak_english, evaltext_english
import b64

'''
repeating-byte XOR with byte string
k can be [0x0a,0x0b] OR 'abc' OR b'abc'
smth like a vigenere cipher
'''
def repeatxor(s, k):
    if(type(s) != bytes):
        return f'repeatxor cannot be used to encrypt a \'{type(S)}\''

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
        return f'invalid key type {type(k)}, must be non empty list/bytes/str'

    # assume k is [0x0a,0x0b,0x10] or smth like that
    if(type(k[0]) != int):
        return f'invalid element in key {type(k[0])}, must be int'

    kptr = 0
    return bytes([ c ^ k[idx % len(k)] for idx,c in enumerate(s) ])

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
    #res = plain.encode('utf8')
    #res = repeatxor(res,key)
    #res = b2hex(res)
    #print(res)

    #a = 'this is a test'
    #b = 'wokka wokka!!!'
    #c = 0x0f
    #print(hamweight(c))
    #print(editdist(a,b))

    with open("files/rhex-6.txt","r") as f:
        buf = f.read()
        buf = buf.replace('\n','') #removes newlines
        buf = b64.decode(buf)

    stat_ks = {}
    for klen in range(1,50):
        s1 = buf[ 0: klen ] # first klen bytes
        s2 = buf[ klen: 2*klen] # klen bytes after first klen bytes
        stat_ks[klen] = editdist(s1,s2)

    for cnt, ks in enumerate(sorted(stat_ks, key=stat_ks.get)):
        print(ks,'distance',stat_ks[ks])
        if(cnt > 10):
            break

    hist = {}
    for klen in sorted(stat_ks, key=stat_ks.get):
        print('Guessing keylength of %d' % klen)

        # chunk up the message
        # and break it
        blocks = []
        bkey = []
        for i in range(klen):
            blocks.append( bytes( buf[j] for j in range(i,len(buf),klen)) )
            bkey.append( sbxbreak_english(blocks[-1],3)[0][0] )

        res = repeatxor(buf,bkey)
        score = evaltext_english(res)
        kstr = ''
        for k in bkey:
            kstr += chr(k)
        hist[kstr] = score

    for cnt, k in enumerate(sorted(hist, key=hist.get, reverse=True)):
        print('rkey:',k,'/score:',hist[k])
        if(cnt > 10):
            break

    # decrypt it
    res = repeatxor(buf, sorted(hist,key=hist.get,reverse=True)[0])
    print(res)
