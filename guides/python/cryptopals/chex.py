#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 1

# Hex literal conversion package
# converts to and from hex literals

# LOOKUP TABLES
hexmap = {
        '0':0x0,'1':0x1,'2':0x2,'3':0x3,'4':0x4,
        '5':0x5,'6':0x6,'7':0x7,'8':0x8,'9':0x9,
        'a':0xa,'b':0xb,'c':0xc,'d':0xd,'e':0xe,
        'f':0xf
        }

hexlkup = [
        '0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f'
        ]

hexlkup_uppercase = [
        '0','1','2','3','4','5','6','7','8','9',
        'A','B','C','D','E','F'
        ]

'''
converts a hex string to lowercase
FOR INTERNAL USE ONLY
'''
def _2lowercase(s):
    s = list(s)
    # change string to lowercase
    for idx,c in enumerate(s):
        if ord(c) >= 65 and ord(c) <= 65+6:
            # c is a uppercase
            s[idx] = chr( ord(c) + 32 )
        elif ord(c) >= 97 and ord(c) <= 97+6:
            # c is a lowercase
            pass
        elif ord(c) >= 48 and ord(c) <= 57:
            # c is a number
            pass
        else:
            # error, invalid char
            return f'invalid hex char at {idx}:\'{c}\''
    return "".join(s)

'''
converts a hex literal string
to byte string
'''
def hex2b(s):
    if len(s) % 2 == 1:
        return f'hex literal has uneven length \'{len(s)}\''

    #lowercase it
    s = _2lowercase(s)
    return bytes([ hexmap[s[idx]] << 4 | hexmap[s[idx+1]] \
        for idx in range(0,len(s),2)])

'''
converts a byte to hex literal
used for pretty printing only
'''
def b2hex(s, lowercase=True):
    out = ''
    if lowercase:
        for c in s:
            out = out + '%02x' % c
    else:
        for c in s:
            out = out + '%02X' % c
    return out


'''
convert hexstring to utf8
returns a string of utf8
'''
def hex2utf8(s):
    if( len(s) % 2 == 1):
        return f'hex literal has uneven length \'{len(s)}\''

    s = _2lowercase(s)

    out = ''
    # go by 2
    for idx in range(0,len(s),2):
        h = hexmap[ s[idx] ]
        l = hexmap[ s[idx+1] ]
        t = (h << 4) | l
        out = out + chr(t)
    return out

'''
convert utf8 to hexstring
returns a string of hex
'''
def utf82hex(s,lowercase=True):
    out = ''
    if lowercase:
        for c in s:
            h = (ord(c) & 0xf0) >> 4
            l = ord(c) & 0x0f
            out = out + hexlkup[h] + hexlkup[l]
    else:
        for c in s:
            h = (ord(c) & 0xf0) >> 4
            l = ord(c) & 0x0f
            out = out +\
                    hexlkup_uppercase[h] +\
                    hexlkup_uppercase[l]
    return out


# TEST DRIVER
if __name__ == "__main__":

    s = '0f12AB'
    res = hex2b(s)
    print(res)
    res = b2hex(res,True)
    print(res)

    s = 'hi a 0123\nA'
    res = utf82hex(s,False)
    print(res)
    res = hex2utf8(res)
    print(res)
