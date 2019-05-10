#ifndef SIMPLESOCK_H
#define SIMPLESOCK_H

short sockgen(short nonblock); //create the socket connection
int sockconn(int sock,char *srv,int port); //connect to a socket
int sockbind(int sock,int port); //bind the socket connection
int sendbuf(int sock, char *sendbuf, short buflen, short timeout_sec); //send via the socket connection
int recvbuf(int sock, char *recvbuf, short buflen, short timeout_sec); //recv via the socket connection

#endif
