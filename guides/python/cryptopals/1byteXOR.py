#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 3

from lkupmap import hexlkup, hexmap
from hexutf8 import hex2utf8_literal, utf82hex_literal

'''
single-byte XOR with literal char
b can be 0x00 - 0xff
'''
def singlebytexor_literal(s, b):
    # every char in s xor b = out
    if type(b) != int:
        return f'can only literal xor with type \'int\', given {type(b)}'
    if len(s) % 2 == 1:
        return f'uneven hexstring length: {len(s)}'

    out = ''
    bh = (b & 0xf0) >> 4
    bl = b & 0x0f
    for idx in range(0,len(s),2):
        th = hexlkup[ hexmap[ s[idx] ] ^ bh ]
        tl = hexlkup[ hexmap[ s[idx+1] ] ^ bl]
        out = out + th + tl
    return out

'''
count occurrences of character in string
'''
def count_literal(s,b):
    r = 0
    for c in s:
        if c == b:
            r = r + 1
    return r

'''
statistical analysis
return list of possible decrypts as tuple with format
(byte-key, score, decrypted text)
'''
def sbxbreak_english(s, rlim = 10):
    # initialize a statistical table
    chrf = [
            ('e',1.5),
            ('t',1.3),
            ('a',1.2),
            ('o',1.2),
            ('i',1.1),
            ('n',1.1),
            ('s',1.1),
            ('h',1.0),
            ('r',1.0)
            ]
    stat = { }
    for f,m in chrf:
        stat[f] = { }

    ka = {} # score track
    kb = {}
    out = []
    # brute force search the keyspace 0x00 - 0xff
    for b in range(0,0xff):
        h = singlebytexor_literal(s,b)
        res = hex2utf8_literal(h)
        for f,m in chrf:
            stat[f][b] = count_literal(res,f)*m
        ka[b] = 0 # initialize scores
        kb[b] = res

    # find statistically plausible onces
    for f,st in stat.items():
        for k,l in st.items():
            ka[k] = ka[k] + l

    for cnt, k in enumerate(sorted(ka, key=ka.get, reverse=True)):
        #print('%d %3d %3.3f' % (cnt,k,ka[k]), kb[k])
        # key, score, decoded
        out.append( (k,ka[k],kb[k]) )
        if(cnt > rlim):
            break

    return out


if __name__ == '__main__':
    ts = 'test string'
    tk = 0xf0
    res = utf82hex_literal(ts)
    res = singlebytexor_literal(res, tk)
    res = singlebytexor_literal(res, tk)
    res = hex2utf8_literal(res)
    print(res)

    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    res = sbxbreak_english(s)[0]
    print(res)

    with open('1hex-4.txt','r') as f:
        for idx, line in enumerate(f):
            if( len(line) % 2 == 1):
                line = line[:-1]
            res = sbxbreak_english(line)[0]
            if(res[1] > 13):
                print(idx,res)
