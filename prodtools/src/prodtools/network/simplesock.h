
#ifndef SIMPLESOCK_H
#define SIMPLESOCK_H



//instructs g++ to not perform name mangling here
//the nested declares are c functions
#ifdef __cplusplus
extern "C"{
#endif

#include <stdint.h>
#include "prodtools/ptdebug.h"

#define SEND_BATCH_SIZE 1024

int sockgen(short nonblock); //create the socket connection
int sockconn(int sock,const char *srv,int port); //connect to a socket
int sockbind(int sock,int port, int reuse_bool); //bind the socket connection
int sendbuf(int sock, char *sendbuf, size_t buflen, int timeout_sec); //send via the socket connection
int recvbuf(int sock, char *recvbuf, size_t buflen, int timeout_sec); //recv via the socket connection
int fixed_recvbuf(int sock, char *recvbuf, size_t buflen, int timeout_sec); //fixed length recv via the socket connection

#ifdef __cplusplus
};
#endif

#endif
