#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 3

from chex import hex2b
#i am too lazy to hardcode a check function for printable/non-printable
import string

# char and multiplier pair
# more common ones have higher weightage
english1 = [
    ('e',1.5),
    ('t',1.3),
    ('a',1.2),
    ('o',1.2),
    ('i',1.1),
    ('n',1.1),
    ('s',1.1),
    ('h',1.0),
    ('r',1.0),
    ('d',1.0),
    ('l',1.0),
    (' ',0.5)
    ]

# http://www.data-compression.com/english.html
english2 = {
        'a': 0.0651738,
        'b': 0.0124248,
        'c': 0.0217339,
        'd': 0.0349835,
        'e': 0.1041442,
        'f': 0.0197881,
        'g': 0.0158610,
        'h': 0.0492888,
        'i': 0.0558094,
        'j': 0.0009033,
        'k': 0.0050529,
        'l': 0.0331490,
        'm': 0.0202124,
        'n': 0.0564513,
        'o': 0.0596302,
        'p': 0.0137645,
        'q': 0.0008606,
        'r': 0.0497563,
        's': 0.0515760,
        't': 0.0729357,
        'u': 0.0225134,
        'v': 0.0082903,
        'w': 0.0171272,
        'x': 0.0013692,
        'y': 0.0145984,
        'z': 0.0007836,
        ' ': 0.1918182
}

'''
fast single-byte XOR
NO CHECKING, assumes s is a byte string and b is an int
'''
def fsbytexor(s, b):
    return bytes([ c ^ b for c in s ])

'''
single byte XOR
perform check that s is a byte string and b is an int
'''
def sbytexor(s, b):
    if type(b) != int or type(s) != bytes:
        return f'invalid type \'{type(s)}\' xor on \'{type(b)}\''
    return fsbytexor(s,b)

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
count printable or unprintable char
'''
def count_print(s,printable=True):
    r = 0
    if printable:
        for c in s:
            if c in string.printable:
                r = r+1
    else:
        for c in s:
            if c not in string.printable:
                r = r+1
    return r

'''
evaluate the likelihood of a bytestring
as english text
https://github.com/ricpacca/cryptopals/blob/c0c945bea99fd77ad5ec3833b4b7047b7014dd3e/S1C03.py#L10
'''
def evaltext_english(s):
    out = 0
    for b in s:
        out = out + english2.get( chr(b).lower(), 0 )
    return out


'''
statistical analysis
return list of possible decrypts as tuple with format
# (KEY_VALUE, SCORE, DECODED_STRING)
'''
def sbxbreak_english(s, rlim = 10, method=2):
    # initialize a statistical table
    if type(s) != bytes:
        print(f'Error on sbxbreak - expect byte string, given \'{type(s)}\'')
        return None

    if method == 1:
        chrf = english1
        stat = { }
        for f,m in chrf:
            stat[f] = { }
        # store unprintable stats
        stat[0] = {}
        # store printable char
        stat[1] = {}
        ka = {} # score track
        kb = {}
        # brute force search the keyspace 0x00 - 0xff
        for b in range(0,0xff):
            h = fsbytexor(s,b)
            try:
                res = h.decode('utf8')
                # count char occurrences of each statistically
                # significant characters (char frequency)
                for f,m in chrf:
                    stat[f][b] = count_literal(res,f)*m
                stat[0][b] = count_print(res,False)*(-2)
                stat[1][b] = count_print(res,True)
            except:
                res = 'utf8 decode error'
            ka[b] = 0 # initialize scores for key
            kb[b] = res # store result

        # find statistically plausible onces
        for f,st in stat.items():
            for k,l in st.items():
                # add up occurences
                ka[k] = ka[k] + l
        # sort
        # finalize by adding out list with tupples of following form:
        # (KEY VALUE, SCORE, DECODED STRING)
        out = []
        for cnt, k in enumerate(sorted(ka, key=ka.get, reverse=True)):
            # key, score, decoded
            out.append( (k,ka[k],kb[k]) )
            if(cnt >= rlim-1):
                break
    elif method == 2:
        stat = {}
        dec = {}
        for b in range(0,0xff):
            dec[b] = fsbytexor(s,b)
            stat[b] = evaltext_english(dec[b])

        out = []
        for cnt, k in enumerate(sorted(stat, key=stat.get, reverse=True)):
            out.append( (k, stat[k], dec[k]) )
            if(cnt >= rlim-1):
                break
    else:
        out = None

    return out


if __name__ == '__main__':
    # string break
    ts = 'test string'
    tk = 0xf0
    res = ts.encode('utf8')
    res = sbytexor(res, tk)
    res = sbytexor(res, tk)
    res = res.decode('utf8')
    print(res)

    # byte break
    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    s = hex2b(s)
    res = sbxbreak_english(s, 5)
    for r in res:
        print(r)
    print(res)

    # file break
    print()
    with open('files/1hex-4.txt','r') as f:
        # for all lines
        for idx, line in enumerate(f):
            # strip the newline
            line = line.strip('\n')
            # convert to bytes
            line = hex2b(line)
            # attempt to break, store most possible answer
            res = sbxbreak_english(line, 10)[0]
            # print only if score greater than 13
            if( res[1] > 1.5):
                print(idx,res)
