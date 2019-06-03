#!/usr/bin/python3
# Simple SSL example
# Alice acts as the client

from OpenSSL import SSL
import socket

def verify_cb(conn, cert, errnum, depth, ok):
    print("Certificate :",cert.get_subject() )
    return ok

if __name__ == "__main__":

    target_host = 'localhost'
    target_port = 40000

    # initialize ssl context
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.set_verify( SSL.VERIFY_PEER, verify_cb )
    ctx.use_privatekey_file( 'alice.skey' )
    ctx.use_certificate_file( 'alice.cert' )
    ctx.load_verify_locations( 'AA.cert' ) #verify
    
    try:
        secure = SSL.Connection( ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM ) )

        print("Attempting to send message")
        secure.connect( (target_host, target_port) )
        secure.send( 'testing over ssl' )
        print("Sent message over ssl")
    except SSL.Error:
        print("SSL Error, connection broken.")
    finally:
        secure.shutdown()
        secure.close()




