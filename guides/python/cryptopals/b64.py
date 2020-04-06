#!/usr/bin/python3
# ToraNova (chia_jason96@live.com)
# cryptopals set 1 challenge 1

# LOOKUP TABLES
b64map = {
        'A':0x00,'B':0x01,'C':0x02,'D':0x03,'E':0x04,
        'F':0x05,'G':0x06,'H':0x07,'I':0x08,'J':0x09,
        'K':0x0a,'L':0x0b,'M':0x0c,'N':0x0d,'O':0x0e,
        'P':0x0f,'Q':0x10,'R':0x11,'S':0x12,'T':0x13,
        'U':0x14,'V':0x15,'W':0x16,'X':0x17,'Y':0x18,
        'Z':0x19,'a':0x1a,'b':0x1b,'c':0x1c,'d':0x1d,
        'e':0x1e,'f':0x1f,'g':0x20,'h':0x21,'i':0x22,
        'j':0x23,'k':0x24,'l':0x25,'m':0x26,'n':0x27,
        'o':0x28,'p':0x29,'q':0x2a,'r':0x2b,'s':0x2c,
        't':0x2d,'u':0x2e,'v':0x2f,'w':0x30,'x':0x31,
        'y':0x32,'z':0x33,'0':0x34,'1':0x35,'2':0x36,
        '3':0x37,'4':0x38,'5':0x39,'6':0x3a,'7':0x3b,
        '8':0x3c,'9':0x3d,'+':0x3e,'/':0x3f
        }

b64lkup = [
        'A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z',
        '0','1','2','3','4','5','6','7','8','9',
        '+','/'
        ]

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
DECODE
pure python base64 to bytes conversion
1 byte is 8bit, 1 b64 is 6bit.
3 byte is 24bit, 4 b64 is 24bit
convert 4 base64 to 3 byte at one time
'''
def decode(s):
    if isb64(s) < 0:
        i = -isb64(s)
        return f'invalid b64 char at {i}:\'{s[i]}\''
    out = []
    # 3F - 0011 1111
    for idx in range(0,len(s),4):
        # high first 2 base64 --XXXXXX w --XX0000
        hi = (b64map[s[idx]] << 2) | ((b64map[s[idx+1]] & 0x30) >> 4)
        if s[idx+2] == '=':
            #me = ((b64map[s[idx+1]] & 0x0f) << 4)
            out.extend([hi])
            break

        # med second and thid --00XXXX w --XXXX00
        me = ((b64map[s[idx+1]] & 0x0f) << 4) | ((b64map[s[idx+2]] & 0x3c) >> 2)

        if s[idx+3] == '=':
            #lo = ((b64map[s[idx+2]] & 0x03) << 6)
            out.extend([hi,me])
            break

        # lo last 2c combined --0000XX w --XXXXXX
        lo = ((b64map[s[idx+2]] & 0x03) << 6) | b64map[s[idx+3]]
        out.extend([hi,me,lo])
    return bytes(out)

'''
ENCODE
pure python bytes to base 64 conversion
convert 3 byte to 4 base64 at one time
'''
def encode(s):
    if type(s) is not bytes:
        print(f'invalid type given for encode. \'bytes\' expected')
    out = ''
    for idx in range(0,len(s),3):
        # b0 XXXX XX00
        b0 = b64lkup[((s[idx] & 0xfc) >> 2)]

        if idx+1 == len(s):
            b1 = b64lkup[((s[idx] & 0x03) << 4)]
            out = out + b0 + b1 + '=='
            break

        # b1 0000 00XX XXXX 0000
        b1 = b64lkup[((s[idx] & 0x03) << 4) | ((s[idx+1] & 0xf0) >> 4)]

        if idx+2 == len(s):
            # b2 ---- ---- 0000 XXXX XX00 0000
            b2 = b64lkup[((s[idx+1] & 0x0f) << 2)]
            out = out + b0 + b1 + b2 + '='
            break
        # b2 ---- ---- 0000 XXXX XX00 0000
        b2 = b64lkup[((s[idx+1] & 0x0f) << 2) | ((s[idx+2] & 0xc0) >> 6)]
        # b3 ---- ---- ---- ---- 00XX XXXX
        b3 = b64lkup[ s[idx+2] & 0x3f ]
        out = out + b0 + b1 + b2 + b3
    return out


if __name__ == "__main__":
    hexstr = b'\xab\xcd\x11\x11'
    hexstr = b'\xab\xcd'
    hexstr = b'\x49\x27\x6D\x20\x6B\x69\x6C\x6C\x69\x6E\x67\x20\x79\x6F\x75\x72\x20\x62\x72\x61\x69\x6E\x20\x6C\x69\x6B\x65\x20\x61\x20\x70\x6F\x69\x73\x6F\x6E\x6F\x75\x73\x20\x6D\x75\x73\x68\x72\x6F\x6F\x6D'

    b64str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    im = encode(hexstr)
    print(im)
    res = decode(im)
    o = ''
    for c in res:
        o = o + '%02X' % c
    print(o)
    if res == hexstr and im == b64str:
        print('ok')
