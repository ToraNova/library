################################################################################
# smsg.py - SOCKET MESSAGE CLASS
# this allows the stream sockets to be used as message sockets, 
# prepending length of msg to the stream before sending.
# this is a very basic solution to sending large messages.
# based truly on :
# https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
# 
# @Author ToraNova
# @mailto chia_jason96@live.com
# @version 1.0
# @date 15 May 2019
################################################################################

import struct # depends on python struct
import pyioneer.support.gpam as gpam

def send(sock,msg):
    # prefix the message with a length variable
    if( type(msg) != bytes ):
        gpam.warn("smsg.send requires the msg to be a bytestream")
        if( type(msg) == str):
            gpam.info("msg type is string. attempting encoding with utf-8")
            msg = msg.encode('utf-8')
        else:
            gpam.error("msg is not string nor bytes. unable to proceed")
            return False
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall( msg )
    return True

def recv(sock):
    # receives the messages from the socket. attributing
    # to the length appended by send_msg
    raw_msglen = recvall(sock,4) #receives the length first
    if not raw_msglen:
        return None #error has occurred
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)

def recvall(sock, sz):
    # receives sz from socket, no timeout
    out = b''
    while len(out) < sz:
        packet = sock.recv(sz-len(out))
        if not packet:
            return None
        out += packet
    return out

# Test not available
if __name__ == "__main__":
    print("Test not available for",__file__)
    pass
    
