/*
 * Line reader example
 * ToraNova, chia_jason96@live.com
 * 2020 Apr 12
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*
 * Sample program to read a file
 * line by line into an array
 */

//#define DEBUG

// line read function,
// This is only applicable for printable texts
// lines -- an unallocated char double pointer
// file  -- an opened file stream, can be stdin too
// returns the number of lines read
char **lineread(FILE *file, int *count){
	*count = 0;
	int mc = 0;
	char tmp, **out;
	long int b, e; //begin and end

	//first PASS to count how many lines
	do{
		tmp = fgetc(file);
		if(tmp == '\n') (*count)++;
	}while(tmp != EOF);
	fseek(file, 0, SEEK_SET); //seek to beginning

	//allocate memory for main out
	out = (char **)malloc((*count)*sizeof(char *));
	while (mc <= *count){
		//read a line
		b = ftell(file);
		do{
			tmp = fgetc(file);
			if(tmp == '\n' || tmp == EOF){
				//stop, rewind to last read and read
				e = ftell(file) - b; //how many chars to read
				e --; //exclude \n or EOF
				break;
			}
		}while(1);
		if(tmp == EOF) break; //break immediately
		fseek(file, b, SEEK_SET);
		out[mc] = (char *)malloc(e); //allocate space
		fread(out[mc], 1, e, file);
#ifdef DEBUG
		printf("scanned: %s\n",out[mc]);
#endif
		//read back the excluded EOF since we seeked past it
		tmp = fgetc(file); //tmp is discarded actually
		mc++; //increment line counter
	}
#ifdef DEBUG
	printf("lines read: %d\n",*count);
#endif
	return out;
}

//DRIVER TEST
int main(int argc, char *argv[]){
	if( argc > 1){
		FILE *input = fopen( argv[1], "r");
		char **temp; int c;
		temp = lineread(input, &c);
		printf("lines read: %d\n",c);
		for(int i=0;i<c;i++){
			printf("%d(%lu): %s\n",i,strlen(temp[i]),temp[i]);
		}
		return 0;
	}
	else{
		return 1;
	}
}
