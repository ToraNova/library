/*
TicTacToe Server
This program waits for 2 incoming socket connection
each conn represents a player.

Players then send numbers 0-8 as position onto the
board. they must receive a turn token before their
move will be registered upon the next send.

0 1 2
3 4 5
6 7 8

chia_jason96@live.com
*/

//toralib
#include"dbg.h"
#include"simplesock.h"
#include"tictactoe.h"

//syslib
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#include<stdio.h>

void handle_client(short clientsock, int turnval ,char *msgbuf, int bufsz); 

int main(int argc, char *argv[]){
	
	log_info("Starting TTT Server for p1 port %d and p2 port %d",P1_PORT,P2_PORT);
	
	struct sockaddr_in p1a,p2a;
	short s1,s2,c1 = -1,c2 = -1; //sockets for p1 and p2
	
	int cli_len = sizeof(struct sockaddr_in); //client len

	char msgbuf[MAXBUFSZ] = {0}; //recv buf size
	int turn = 1; //player 1 starts first
 
 	//Create socket
 	s1 = sockgen(1);
	s2 = sockgen(1);
	if(s1 < 0 || s2 < 0){log_err("Couldn't create socket...");return 1;}

	//bind the socket
	if(sockbind(s1,P1_PORT) < 0 || sockbind(s2,P2_PORT) < 0){log_err("Binding failed");return 1;}
	
	//listen for incoming conn
	log_info("Listening on port %d and %d for clients",P1_PORT,P2_PORT);
	listen(s1,3);
	listen(s2,3); 

	//Accept incoming conn
	while(1){
		//infinite loop to wait for incoming conn
		if(c1 < 0)c1 = accept( s1 , (struct sockaddr *)&p1a, (socklen_t*)&cli_len);
		if(c2 < 0)c2 = accept( s2 , (struct sockaddr *)&p2a, (socklen_t*)&cli_len);
		if(c1 >= 0 && c2 >= 0){
			log_info("Both clients connected...");
			break;
		}
	}
	log_info("Initializing Board");
	while(1){
		log_info("Currently Turn for Player(Client) %d",turn);
		memset(msgbuf,'\0', MAXBUFSZ);
		switch(turn){
			case 1:
				handle_client(c1,turn,msgbuf,MAXBUFSZ);
				turn = 2;
			break;
			case 2:
				handle_client(c2,turn,msgbuf,MAXBUFSZ);
				turn = 1;
			break;
			default:
				turn = 1;
			
		}
	}
	close(s1);
	close(s2);
	return 0;
}

void handle_client(short clientsock, int turnval ,char *msgbuf, int bufsz){
	char tokenv[MAXBUFSZ] = "tok";
	//for flushing purposes
	//if(recv(clientsock, msgbuf, MAXBUFSZ, 0) < 0)log_err("Failed to recv from socket");
	//memset(msgbuf,'\0', MAXBUFSZ);
	//end of flush
	if(send(clientsock, tokenv , strlen(tokenv) , 0) < 0)log_err("Failed to send token");
	log_info("Awaiting input from client %d",turnval);
	if(recv(clientsock, msgbuf, MAXBUFSZ, 0) < 0)log_err("Failed to recv from socket");
	log_info("Input from client %d: %s",turnval,msgbuf);
}





