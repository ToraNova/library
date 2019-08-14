/*
simple socket connection library for c

written for a machine learning tutorial
chia_jason96@live.com

guided strongly by (credits to the original author)
https://aticleworld.com/socket-programming-in-c-using-tcpip/
*/
#include"dbg.h"
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<stdlib.h>
#include<errno.h>

#include"simplesock.h"

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

int sockbind(int sockobj, int portnum){
	//bind the created socket
	int retval = -1;
	struct sockaddr_in remote={0};

	//setup connection params
	remote.sin_addr.s_addr = htonl(INADDR_ANY);
	remote.sin_family = AF_INET;
	remote.sin_port = htons(portnum);

	retval = bind(sockobj,(struct sockaddr *)&remote,sizeof(struct sockaddr_in));
	log_info("Socket bound to port %d returns %d",portnum,retval);
	return retval;
}

int sendbuf(int sockobj, char *sendbuffer, short buflen, short timeout_sec){
	//send via the socket connection

	int retval = -1;
	struct timeval timeout; //setup the timeout
	timeout.tv_sec = timeout_sec;
	timeout.tv_usec = 0; //usec must be named to prevent out of domain errors

	if(setsockopt(sockobj,SOL_SOCKET, SO_SNDTIMEO, &timeout,sizeof(struct timeval)) < 0){
		log_err("Socket set options failed. %d",timeout_sec);
		perror("Error :");
		return -1;
	}
	//code enters here when setup is successful
	retval = send(sockobj, sendbuffer, buflen,0);
	log_info("Buffer %s of size %d sent with retval:%d",sendbuffer,buflen,retval);
	return retval;
}

int recvbuf(int sockobj, char *recvbuffer, short buflen, short timeout_sec){
	//recv via the socket connection

	int retval = -1;
	struct timeval timeout;
	timeout.tv_sec = timeout_sec;
	timeout.tv_usec = 0; //usec must be named to prevent out of domain errors

	if(setsockopt(sockobj,SOL_SOCKET, SO_RCVTIMEO, &timeout,sizeof(struct timeval)) < 0){
		log_err("Socket set options failed. %d",timeout_sec);
		perror("Error :");
		return -1;
	}
	//code enters here when setup is successful
	retval = recv(sockobj, recvbuffer, buflen,0);
	log_info("Buffer %s of size %d recv with retval:%d",recvbuffer,buflen,retval);
	return retval;
}

