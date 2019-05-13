/*
Test program for the simplesock pkg
SERVER TEST PROGRAM

chia_jason96@live.com
*/

//toralib
#include"dbg.h"
#include"simplesock.h"

//syslib
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#include<stdio.h>

#define MAXBUFSZ 	256

int main(int argc, char *argv[]){
	log_info("Starting socket server test program");
	
	int pnum = 10001;
	struct sockaddr_in cli;

	short ssock,csock; //server socket and client socket
	
	int cli_len = sizeof(struct sockaddr_in);
	char msgbuf[MAXBUFSZ] = {0};
 
 	//Create socket
 	ssock = sockgen(0);
	if(ssock < 0){log_err("Couldn't create socket...");return 1;}

	//bind the socket
	if(sockbind(ssock,pnum) < 0){log_err("Binding failed");return 1;}
	
	//listen for incoming conn
	log_info("Listening on port %d",pnum);
	listen(ssock, 3); 

	//Accept incoming conn
	while(1){
		//infinite loop to wait for incoming conn
		csock = accept( ssock, (struct sockaddr *)&cli, (socklen_t*)&cli_len);
		if(csock < 0){log_err("Failed to accept conn");return 1;}
		log_info("Conn accepted");
		memset(msgbuf,'\0', MAXBUFSZ);
		if( recv(csock, msgbuf, MAXBUFSZ, 0) < 0){log_err("Failed to recv from socket");break;}
		log_info("Client msg : %s",msgbuf);
		//echo back
		if( send(csock, msgbuf, strlen(msgbuf),0) < 0){log_err("Failed to echo back");break;}
		close(csock); //close the client socket conn
		
	}	
	close(ssock);
	return 0;
}





