/*
 * This is a code vulnerable to 32bit ROP
 * Based on the example retrieved from :
 * http://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html
 * 64bit version, and honestly much more interesting :
 * https://crypto.stanford.edu/~blynn/rop/
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//secure is not called.
void secure(){
	printf("Shell Access\n");
	system("/bin/bash");
}

//the following function is vulnerable for ROP exploit
void vulnerable( char *ptr ){
	char buffer[100];
	strcpy( buffer, ptr );
	return;
}

//main function
int main(int argc, char **argv){

	char fixedbuffer[64];
	printf("%p\n",fixedbuffer);//allow us to find the buffer
	fgets(fixedbuffer, 100, stdin); //badly designed
	vulnerable( fixedbuffer );

	return 0;
}
