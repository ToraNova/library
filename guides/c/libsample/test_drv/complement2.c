#include<stdio.h>
#include<stdlib.h>
#define MAXLEN 256

//function proto
int getlength(char *);
int getindex(char,const char *,int);
char *lookuptable(char *, int);
void inchexarr(char *, int); 
void toprintable(char *,int);

int main(int argc, char *argv[]){
	
	int i,j; //counters
	int hexlen; //length of hex

	if(argc != 2){
		printf("com2 only accept 1 argument <HEXvalue> to perform 2's complement\n");
		printf("e.g. com2 ffff\n");
		return 1;
	}

	hexlen = getlength(argv[1]); //obtain the length of the hex
	if(hexlen == -1){
		printf("Error has occurred. Hex string with no null terminator\n");
		return 1;
	}
	else printf("Hex has %d hex digits\n",hexlen);
	
	char *hexarr = lookuptable(argv[1], hexlen);
	inchexarr(hexarr, hexlen);
	toprintable(hexarr,hexlen);
	printf("2's complement : %s\n",hexarr);
	return 0;
}

//defines
int getlength(char *target){
	//obtains the length of the string
	int i;
	for(i=0;i<MAXLEN;i++) {
		if(target[i]==0x00) return i;
	}
	return -1; //invalid string (no null terminator)
}

int getindex(char target, const char *lookup, int len){
	//find the target char in the lookup table, returning the index
	int i;
	for(i=0;i<len;i++) {
		if(target == lookup[i]) return i;
	}
	return -1;
}
	

char *lookuptable(char *arr, int len){
	//obtain the hex value by finding the index of the lookup table
	char *out = (char *) malloc( len );
	const char *lookup0 = "0123456789abcdef"; //hex 16 digit
	int i;
	for(i=0;i<len;i++) {
		out[i] = getindex( arr[i], lookup0, 16);
		out[i] = out[i] ^ 0x00f; //flipping
	}
	return out;
}

void toprintable(char *target,int len){
	//convert the hex values back to printable bytes
	const char *lookup0 = "0123456789abcdef"; //hex 16 digit
	int i;
	for(i=0;i<len;i++){
		target[i] = lookup0[target[i]];
	}
}

void inchexarr(char *target, int len){
	
	int i;
	_Bool c = 1; //carry flag
	for(i=len-1;i>=0;i--){
		if(c){
			target[i] += 1;
			if(target[i] >= 16) target[i] = 0;
			else c = 0;
		}
	}	
}

		




