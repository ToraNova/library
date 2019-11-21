/*
 * This is a single file library based on John's base64 example on the web
 * All credits to him. (John Schember)
 * https://nachtimwald.com/2017/11/18/base64-encode-and-decode-in-c/
 *
 * edited and put together in a file by ToraNova
 * modified to automatically ignore newline, but will output newline
 * after 76 chars (RFC 2045)
 * chia_jason96@live.com
 * github.com/toranova
 */

#include "jbase64.h"

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BASE64_DEFAULT_WRAP 76

/*
 * Thank god for these
 */
//encoding table
const char b64chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

//decoding table
const int b64invs[] = { 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58,
	59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5,
	6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
	21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28,
	29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
	43, 44, 45, 46, 47, 48, 49, 50, 51 };

/*
 * This is used to generate the inversion table
 * for speed, we will use the lookup instead of generating one
 * for every decode
 */
//
/*
void b64_generate_decode_table()
{
	int    inv[80];
	size_t i;

	memset(inv, -1, sizeof(inv));
	for (i=0; i<sizeof(b64chars)-1; i++) {
		inv[b64chars[i]-43] = i;
	}
}
*/

//compute b64 size based on input size of byte arr
//wrap -- how many characters after to insert a line wrap (\n)
//by default this should be 76. set to 0 to disable line wrap
size_t b64_encoded_size(size_t inlen, size_t wrap){
	size_t ret;

	ret = inlen;
	if (inlen % 3 != 0){
		ret += 3 - (inlen % 3);
	}
	ret /= 3;
	ret *= 4;

	//count how many additional slots we need for \n
	if(wrap > 0 && ret > wrap ){
		ret += ret / wrap ;
	}

	return ret;
}

//compute binary size required to store decoded base64 data
size_t b64_decoded_size(const char *in){
	size_t len;
	size_t ret;
	size_t i;

	if (in == NULL)
		return 0;

	len = strlen(in);
	ret = len / 4 * 3;

	for (i=len; i-->0; ) {
		//ignore padding and linewraps
		if (in[i] == '=' || in[i] == '\n') {
			ret--;
		} else {
			break;
		}
	}

	return ret;
}

//encode binary to base64
//wrap -- how many characters to insert a line wrap (\n) after
//by default this should be 76 according to RFC2045
char *b64_encode(const unsigned char *in, size_t len, size_t wrap){
	char   *out;
	size_t  elen;
	size_t  i;
	size_t  j;
	size_t  v;

	if (in == NULL || len == 0)
		return NULL;

	//obtain output size
	elen = b64_encoded_size(len, wrap);
	out  = (char *)malloc(elen+1);
	out[elen] = '\0';

	for (i=0, j=0; i<len; i+=3, j+=4) {

		//line wrap support
		if(j >= wrap && wrap > 0){
			out[j++] = '\n';
			wrap += wrap;
		}

		//push 3 bytes into an int
		v = in[i];
		v = i+1 < len ? v << 8 | in[i+1] : v << 8;
		v = i+2 < len ? v << 8 | in[i+2] : v << 8;

		//obtain lookup
		out[j]   = b64chars[(v >> 18) & 0x3F];
		out[j+1] = b64chars[(v >> 12) & 0x3F];
		if (i+1 < len) {
			out[j+2] = b64chars[(v >> 6) & 0x3F];
		} else {
			out[j+2] = '=';
		}
		if (i+2 < len) {
			out[j+3] = b64chars[v & 0x3F];
		} else {
			out[j+3] = '=';
		}

	}
	return out;
}

//decode base64 to binary
//remember to free the memory once done
//return 1 upon success and 0 on fail
unsigned char *b64_decode(const char *in)
{
	size_t outlen = b64_decoded_size(in);
	unsigned char *out = (unsigned char *)malloc(outlen+1);//include null terminator
	size_t len;
	size_t i;
	size_t j;
	int    v;

	if (in == NULL)
		return NULL;

	len = strlen(in);
	for (i=0; i<len; i++) {
		if (!b64_isvalidchar(in[i])) {
			return NULL;
		}
	}

	for (i=0, j=0; (i+3)<len; i+=4, j+=3) {

		//skip the newlines
		if( in[i] == '\n' ){
			i++;
			if((i+3) >= len){
				break;
			}
		}
		v = b64invs[in[i]-43];
		v = (v << 6) | b64invs[in[i+1]-43];
		v = in[i+2]=='=' ? v << 6 : (v << 6) | b64invs[in[i+2]-43];
		v = in[i+3]=='=' ? v << 6 : (v << 6) | b64invs[in[i+3]-43];

		out[j] = (v >> 16) & 0xFF;
		if (in[i+2] != '=')
			out[j+1] = (v >> 8) & 0xFF;
		if (in[i+3] != '=')
			out[j+2] = v & 0xFF;
	}
	if(j < outlen && i < len){
		//probably decode fail
		return NULL;
	}

	return out;
}

//check if it is a valid base64 alphabet
// ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
int b64_isvalidchar(char c)
{
	if (c >= '0' && c <= '9')
		return 1;
	if (c >= 'A' && c <= 'Z')
		return 1;
	if (c >= 'a' && c <= 'z')
		return 1;
	if (c == '+' || c == '/' || c == '=' || c == '\n' )
		return 1;
	return 0;
}

/*
 * Test function
 */
int main(int argc, char **argv)
{
	const char *data = "test to ensure that the decoder works correctly 1232133421awdawd";
	char *enc;
	char *out;

	printf("enc_in (%lu): %s\n", strlen(data), data);
	enc = b64_encode((const unsigned char *)data, strlen(data), BASE64_DEFAULT_WRAP);
	//enc = b64_encode((const unsigned char *)data, strlen(data), 0);
	printf("enc_out (%lu):\n%s\n", strlen(enc), enc);

	/* +1 for the NULL terminator. */
	out = (char *)b64_decode(enc);
	if( out == NULL ){
		printf("Decode failure\n");
		return 1;
	}
	out[b64_decoded_size(enc)] = '\0'; //for strings
	printf("dec_ou (%lu): %s\n", strlen(out), out);
	free(out);
	return 0;
}





