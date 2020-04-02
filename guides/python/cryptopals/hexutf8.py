#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals helper

from lkupmap import hexlkup, hexmap

'''
convert utf8 to hexstring
returns a string of hex
'''
def utf82hex_literal(s):
    out = ''
    for c in s:
        h = (ord(c) & 0xf0) >> 4
        l = ord(c) & 0x0f
        out = out + hexlkup[h] + hexlkup[l]
    return out

'''
convert hexstring to utf8
returns a string of utf8
'''
def hex2utf8_literal(s):
    if( len(s) % 2 == 1):
        return f'invalid hexstring length {len(s)}'
    out = ''
    # go by 2
    for idx in range(0,len(s),2):
        h = hexmap[ s[idx] ]
        l = hexmap[ s[idx+1] ]
        t = (h << 4) | l
        out = out + chr(t)
    return out

if __name__ == '__main__':
    s = 'hi a 0123\nA'

    res = utf82hex_literal(s)
    print(res)
    res = hex2utf8_literal(res)
    print(res)
