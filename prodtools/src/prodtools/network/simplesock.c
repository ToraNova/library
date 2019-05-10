/*
simple socket connection library for c

written for a machine learning tutorial
chia_jason96@live.com

guided strongly by (credits to the original author)
https://aticleworld.com/socket-programming-in-c-using-tcpip/
*/

#include "simplesock.h"

#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<stdlib.h>
#include<errno.h>

extern int errno;

int sockgen(short nonblock){
	//create the socket connection
	int sockobj;
	sockobj = socket(
		AF_INET,
		nonblock? SOCK_STREAM | SOCK_NONBLOCK : SOCK_STREAM ,
		0);
	return sockobj;
}

int sockconn(int sockobj, const char *srvaddr,int portnum){
	//connect to a socket server
	int retval = -1;
	struct sockaddr_in remote={0};

	//setup connection params
	remote.sin_family = AF_INET;
	remote.sin_addr.s_addr = inet_addr(srvaddr);
	remote.sin_port = htons(portnum);

	//attempt to connect, obtaining the result code as retval.
	retval = connect(sockobj, (struct sockaddr *)&remote, sizeof(struct sockaddr_in));
	log_info("Connection to %s on port %d returns %d",srvaddr,portnum,retval);
	return retval;
}

int sockbind(int sockobj, int portnum, int reuse_bool){
	//bind the created socket
	//if reuse_bool is set to 1, binds immediately again
	int retval = -1;
	struct sockaddr_in remote={0};

	//setup connection params
	remote.sin_addr.s_addr = htonl(INADDR_ANY);
	remote.sin_family = AF_INET;
	remote.sin_port = htons(portnum);

	if(setsockopt(sockobj,SOL_SOCKET, SO_REUSEADDR, &reuse_bool,sizeof(int)) < 0){
		log_err("Socket set options failed. %d",reuse_bool);
		perror("sockbind : setsockopt");
		return -1;
	}

	retval = bind(sockobj,(struct sockaddr *)&remote,sizeof(struct sockaddr_in));
	log_info("Socket bound to port %d returns %d",portnum,retval);
	return retval;
}

int sendbuf(int sockobj, char *sendbuffer, size_t buflen, int timeout_sec){
	//send via the socket connection

	struct timeval timeout; //setup the timeout
	timeout.tv_sec = timeout_sec;
	timeout.tv_usec = 0;

	uint32_t bleft = buflen;
	uint32_t thisbatch = 0;
	uint32_t ptrindex = 0;
	int sent = 0;

	//perform timeout setup
	if(setsockopt(sockobj,SOL_SOCKET, SO_SNDTIMEO, &timeout,sizeof(struct timeval)) < 0){
		log_err("Socket set options failed. %d",timeout_sec);
		perror("sendbuf : setsockopt");
		return -1;
	}
	//code enters here when setup is successful
	while( bleft > 0 ){
		if(buflen > SEND_BATCH_SIZE) thisbatch = SEND_BATCH_SIZE;
		else thisbatch = bleft;
		sent = send(sockobj, sendbuffer+ptrindex, thisbatch,0);
		if(sent == -1)break;
		ptrindex += sent;
		bleft -= sent;
	}
	log_info("Buffer %s of size %zu sent with retval:%d",sendbuffer,buflen,sent);
	return sent;
}

int recvbuf(int sockobj, char *recvbuffer, size_t buflen, int timeout_sec){
	//recv via the socket connection

	int retval = -1;
	struct timeval timeout;
	timeout.tv_sec = timeout_sec;
	timeout.tv_usec = 0;

	//perform timeout setup
	if(setsockopt(sockobj,SOL_SOCKET, SO_RCVTIMEO, &timeout,sizeof(struct timeval)) < 0){
		log_err("Socket set options failed. %d",timeout_sec);
		perror("recvbuf : setsockopt");
		return -1;
	}
	//code enters here when setup is successful
	retval = recv(sockobj, recvbuffer, buflen,0);
	log_info("Buffer %s of size %zu recv with retval:%d",recvbuffer,buflen,retval);
	return retval;
}

int fixed_recvbuf(int sockobj, char *recvbuffer, size_t buflen, int timeout_sec){
	//recv via the socket connection
	//must receive buflen or else it will not stop.

	int retval = -1;
	struct timeval timeout;
	timeout.tv_sec = timeout_sec;
	timeout.tv_usec = 0;

	uint32_t bleft = buflen;
	uint32_t thisbatch = 0;
	uint32_t ptrindex = 0;
	int brecv = 0;

	//perform timeout setup
	if(setsockopt(sockobj,SOL_SOCKET, SO_RCVTIMEO, &timeout,sizeof(struct timeval)) < 0){
		log_err("Socket set options failed. %d",timeout_sec);
		perror("fixed_recvbuf : setsocktopt");
		return -1;
	}
	//code enters here when setup is successful
	while( bleft > 0 ){
		if(buflen > SEND_BATCH_SIZE) thisbatch = SEND_BATCH_SIZE;
		else thisbatch = bleft;
		brecv = recv(sockobj, recvbuffer+ptrindex, thisbatch,0);
		if(brecv == -1)break;
		ptrindex += brecv;
		bleft -= brecv;
	}
	log_info("Buffer %s of size %zu recv with retval:%d %d",recvbuffer,buflen,brecv,ptrindex);
	return brecv == -1 ? brecv : ptrindex ;
}
