/*
 * Pure C implementation of a base64 encoder
 * converts a string of characters into base64
 *
 */

#include<stdio.h>
#include<stdlib.h>

void threefour( char *, char *, unsigned int);
char *ch2base64( char *, unsigned int);

int main(int argc, char *argv[]){
	char tmpbuf[4];
	char *mbuf;

	if( argv[1] == NULL ){
		printf("Usage: ch2b64 <string>\n");
		printf("Converts <string> into base64 encoding\n");
		return 1;
	}

	//first obtains length of the input string
	unsigned int len = 0;
	while( argv[1][len] != '\0' ){
		len++;
	}
	//printf("Length:%u\n",len);

	mbuf = ch2base64( argv[1], len);
	printf("%s\n",mbuf);

	return 0;
}

/* char string to base64 string
 * converts a string to base64
 * uses threefour function
 * please rmb to free the returned pointer
 */
char *ch2base64( char *src, unsigned int srclen){

	int allocsize;
	if(srclen < 3)allocsize = 4;
	else allocsize = ((double)srclen)*(4.0/3.0) + 1;
	char *out = (char *)malloc( allocsize );
	unsigned int ctr0 = 0;
	unsigned int ctr1 = 0;

	while(srclen - ctr1 > 0){
		if(srclen - ctr1 >= 3){
			threefour( out + ctr0, src + ctr1, 3);
		}else{
			threefour( out + ctr0, src + ctr1, srclen-ctr1);
			break;
		}
		ctr0 += 4;
		ctr1 += 3;
	}
	return out;
}

/* threefour
 * convert 3 bytes to 4 base64
 * n is usually 3 unless used at the end to pad
 * written by ToraNova
 * warn: make sure target has at least 4 char location
 * and src has at least 3 char location
 */
void threefour( char *target, char *src, unsigned int n ){
	int i;
	const char lkup[65] =
		    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		    "abcdefghijklmnopqrstuvwxyz"
		    "0123456789+/";
	//pre assign
	target[2] = '=';
	target[3] = '=';

	target[0] = lkup[(src[0] & 0xfc) >> 2];
	target[1] = lkup[(src[0] & 0x03) << 4 |
			(src[1] & 0xf0) >> 4];
	if(n < 2)return;
	target[2] = lkup[(src[1] & 0x0f) << 2 |
			(src[2] & 0xc0) >> 6];
	if(n < 3)return;
	target[3] = lkup[(src[2] & 0x3f)];
	return;
}




