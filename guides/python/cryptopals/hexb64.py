#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 1

from lkupmap import b64lkup, hexlkup, b64map, hexmap

'''
pure python hex to base 64 literally
takes a HEX representation '0123FF' and convert it to base64
return an error msg if invalid char detected
return a the base64 string on success
'''
def hex2b64_literal(s):
    # hex is 4bit, base64 is 6bit per char
    # 3 hex char is 2 b64 char
    # f6d = 9t ? decimal : 3949
    out = ''

    # change string to lowercase
    for idx,c in enumerate(s):
        if ord(c) >= 65 and ord(c) <= 65+6:
            # c is a uppercase
            c = chr( ord(c) + 32 )
        elif ord(c) >= 97 and ord(c) <= 97+6:
            # c is a lowercase
            pass
        elif ord(c) >= 48 and ord(c) <= 57:
            # c is a number
            pass
        else:
            # error, invalid char
            return f'invalid hex char at {idx}:\'{c}\''

    idx = 0
    # continue if we have 3 hex for processing
    while idx+2 < len(s):
        # compute 'high' and 'low' base64 char
        h = (hexmap[s[idx]] << 2) | ((hexmap[s[idx+1]] & 0xc) >> 2)
        l = ((hexmap[s[idx+1]] & 0x3) << 4) | hexmap[s[idx+2]]
        out = out + b64lkup[h] + b64lkup[l]
        idx = idx + 3
    if( idx+1 < len(s) ):
        # 2 left, add 2 =
        h = (hexmap[s[idx]] << 2) | ((hexmap[s[idx+1]] & 0xc) >> 2)
        l = ((hexmap[s[idx+1]] & 0x3) << 4)
        out = out + b64lkup[h] + b64lkup[l] + '=='
        idx = idx + 2
    elif( idx < len(s) ):
        # 1 left, add 1 =
        out = out + b64lkup[(hexmap[s[idx]] << 2)] + '='
        idx = idx + 1
    return out

'''
checks if string is a valid b64
return negative index if false,
else, return a positive number (1)
'''
def isb64(s):
    #ensure string is valid
    for idx,c in enumerate(s):
        if c not in b64lkup:
            if c == '=':
                if idx == len(s)-1:
                    # last char, valid
                    break
                elif idx == len(s)-2:
                    # second last, last should be padded
                    if s[idx+1] == '=':
                        break
            return -idx
    return 1

'''
pure python base 64 to hex literally
takes a HEX representation 'abWZ30=' and convert it to base64
return an error msg if invalid char detected
return a the base64 string on success
'''

def b642hex_literal(s):
    out = ''
    if(isb64(s) < 0):
        i = -isb64(s)
        return f'invalid b64 char at {i}:\'{s[i]}\''

    idx = 0
    # continue if we have 2 b64 for processing
    while idx+1 < len(s):
        # compute 'high' and 'low' base64 char
        h = 0
        m = 0
        l = 0
        if s[idx] == '=' :
            break
        h = (b64map[s[idx]] & 0x3c) >> 2
        if s[idx+1] == '=':
            out = out + hexlkup[h]
            break
        else:
            m = ((b64map[s[idx]] & 0x03) << 2) | ((b64map[s[idx+1]] & 0x30) >> 4)
            l = b64map[s[idx+1]] & 0x0f
            out = out + hexlkup[h] + hexlkup[m] + hexlkup[l]
        #print(idx, s[idx], s[idx+1], out, h, m, l)
        idx = idx + 2

    #ensure hex output is even number
    if(len(out) % 2 == 1):
        #trim last
        if( out[-1] == '0' ):
            out = out[:-1]
    return out

if __name__ == "__main__":
    # test script
    import time

    #res = 'abcd1111'
    res = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    stime = time.process_time()
    res = hex2b64_literal(res)
    etime = time.process_time()
    print( (etime - stime)*1000 ,'ms')
    print(res)
    stime = time.process_time()
    res = b642hex_literal(res)
    etime = time.process_time()
    print( (etime - stime)*1000 ,'ms')
    print(res)


