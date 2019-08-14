/*
 * Sample File IO
 * ToraNova Aug 14 2019
 * compile with:
 * gcc file.c -o file
 */
#include<stdio.h>
#include<stdlib.h>

#define MAXBUFSIZE 1024

int main(){
	//Declares a file pointer
	FILE *fptr;
	int rc;

	// constant chars
	const char *filename = "sample.txt";
	/*
	 * Modes
	 * r 	- reading
	 * w 	- writing (write from beginning)
	 * r+	- read/write
	 * w+	- read/write, truncates to pos 0 and write
	 * a	- appending (do not erase)
	 * a+	- reading start from beginning, writing is appended
	 * b	- binary mode [APPEND THIS i.e., rb, a+b]
	 *
	 */
	//define mode
	const char *mode = "r+"; //write mode
	char buffer[MAXBUFSIZE]; //readbuffer
	char tmp;

	//opens the stream
	fptr = fopen(filename, mode);

	//write to file
	fprintf( fptr, "Hello World ! File written in mode: %s\n", mode);
	rc = fclose(fptr); //close and write the file, returns 0 on success

	//reading
	fptr = fopen(filename, "r");
	printf("Current FPTR pos:%d\n", ftell(fptr));

	//reads the first char
	tmp = fgetc( fptr );
	fputc( tmp, stdout);
	fputc( '\n', stdout);
	printf("Current FPTR pos:%d\n", ftell(fptr));

	/*
	 * SEEK_SET - set origin as beginning of file
	 * if offset = 0, then this is same as
	 * rewind(fptr);
	 *
	 * SEEK_CUR - set origin to current position of ftell
	 * if offset = 0, this does nothing
	 *
	 * SEEK_END - set origin to end of file.
	 * if offset = 0, this goes to end of file
	 *
	 * offset (2nd arg number of bytes/char to offset from origin)
	 */
	fseek( fptr, 0, SEEK_SET);
	printf("Current FPTR pos:%d\n", ftell(fptr));
	while( fgets( buffer, MAXBUFSIZE, fptr) != NULL){
		for(rc=0; rc< MAXBUFSIZE; rc++){
			if(buffer[rc] == '\n')break;
		}
		fputs( buffer, stdout );
		printf("char:%d\n",rc);
	}
	rc = fclose(fptr);
	return rc;
}
