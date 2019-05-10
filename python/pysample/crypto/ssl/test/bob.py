#!/usr/bin/python3
# Simple SSL example
# Bob acts as the server

from OpenSSL import SSL
import socket, select

def verify_cb(conn, cert, errnum, depth, ok):
    print("Certificate :", cert.get_subject() )
    return ok

if __name__ == "__main__":

    target_port = 40000

    # initialize ssl context
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.set_options(SSL.OP_NO_SSLv2)
    ctx.set_verify( SSL.VERIFY_PEER|SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_cb )
    ctx.use_privatekey_file( 'bob.pkey' )
    ctx.use_certificate_file( 'bob.cert' )
    ctx.load_verify_locations( 'AA.cert' ) #verify
    
    try:
        secure = SSL.Connection( ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM ) )
        secure.bind(('',target_port))
        secure.listen(3)
        #server.setblocking(0)

        print("Awaiting incoming message on port",str(target_port))
        cli,addr = secure.accept()
        print("Connection established with",addr)

        # sets a 1 second timeout
        print("Timeout recv of 1024 bytes for",addr)
        ret = cli.recv(1024) 
        print("Received",ret)

    except Exception as e:
        print("Exception has occurred :",str(e))

    finally:
        try:
            #secure.shutdown()
            secure.close()
            #cli.shutdown()
            cli.close()
        except Exception as e:
            print("Error while shutting down sockets:",str(e))




