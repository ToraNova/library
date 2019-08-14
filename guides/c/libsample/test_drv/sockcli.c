/*
Test program for the simplesock pkg
CLIENT TEST PROGRAM

chia_jason96@live.com
*/

//toralib
#include"dbg.h"
#include "simplesock.h"

//syslib
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#include<stdio.h>

#define MAXBUFSZ 	256
#define TIMEOUT_S	10

int main(int argc, char *argv[]){
	log_info("Starting socket client test program");

	char *hostaddr = "127.0.0.1";
	int portnum = 10001;

	char sbuf[MAXBUFSZ] = "TORA";
	char rbuf[MAXBUFSZ] = {0};
	int readcount;
	
	short tsock;
 
 	//Create socket
 	tsock = sockgen(0);
	if(tsock == -1){log_err("Couldn't create socket...");return 1;}

	//attempting to connect to server	
	if( sockconn(tsock,"127.0.0.1",10001) < 0){log_err("Conn error!");return 1;}

	log_info("Connection established with %s on port %d",hostaddr,portnum);
	log_info("Sending %s to server",sbuf);

	sendbuf(tsock, sbuf , strlen(sbuf),10);
	readcount = recvbuf(tsock, rbuf, MAXBUFSZ,10);

	log_info("Reply from server : %s",rbuf);

	close(tsock);
	
	return 0;
}





