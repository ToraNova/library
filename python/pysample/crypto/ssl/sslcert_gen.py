#!/usr/bin/python3

# Sample code to generate certificate chains (or self signed)
# using pyopenssl
# original author : msabramo
# https://github.com/msabramo/pyOpenSSL/blob/master/examples/mk_simple_certs.py
# edited by ToraNova for python3

from OpenSSL import crypto
from certgen import createKeyPair, createCertRequest, createCertificate
from certgen import TYPE_RSA, TYPE_DSA

def write_certkey_pem( fname, key, cert ):
    with open(fname+'.pkey','w') as f:
        f.write( crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode('utf-8') )
    with open(fname+'.cert','w') as f:
        f.write( crypto.dump_certificate( crypto.FILETYPE_PEM, cert).decode('utf-8') )
    return

if __name__ == "__main__":

    AA_keysize = 2048
    cert_authority = 'Adhoc Authority'

    # creates the keypair of size 1024
    AA_key = createKeyPair(TYPE_RSA, AA_keysize)

    # creates the cert request with the key and name
    AA_req = createCertRequest( AA_key, CN=cert_authority)

    # creates the cert for 5 years
    valid_dur = 60*60*24*365*5

    # certificate generation
    # Adhoc Authority signs its own key (self signed)
    AA_cert = createCertificate( AA_req, (AA_req, AA_key), 0, (0, valid_dur)) 

    write_certkey_pem( 'AA', AA_key, AA_cert )

    # now AA issues (or don't) to some parties
    AA_issue = ( AA_cert, AA_key)
    issue_dur = 60*60*24*365*1
    parties = [
            ('alice','Alice (signed AA)',2048, AA_issue, 12345),
            ('bob','Bob (signed AA)',2048, AA_issue , 56789),
            ('mallory','Mallory (self signed)',2048,None, 99999)
            ]

    for ( fname, cname, keysize, issue, serial ) in parties:
        
        pkey = createKeyPair( TYPE_RSA, keysize )
        preq = createCertRequest( pkey, CN=cname )
        if issue is None:
            # self sign instead
            pcrt = createCertificate( preq, (preq, pkey), serial, (0, issue_dur))
        else:
            # signed by AA
            pcrt = createCertificate( preq, issue, serial, (0, issue_dur))
        write_certkey_pem( fname, pkey, pcrt )




