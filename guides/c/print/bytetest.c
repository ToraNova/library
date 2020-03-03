/*
 * Making sure the byte print is working correctly
 */

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]){

	char testbuf[] = { 0x3F, 0x40, 0x50, 0x60, 0x7A };
	size_t i;
	for(i=0;i<5;i++){
		printf("%02X",testbuf[i]);
	}
	printf("\n");

	return 0;
}
