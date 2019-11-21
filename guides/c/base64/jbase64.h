/*
 * Header file for jbase64 library
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

#include <stddef.h>

#define BASE64_DEFAULT_WRAP 76

//compute b64 size based on input size of byte arr
//wrap -- how many characters after to insert a line wrap (\n)
//by default this should be 76. set to 0 to disable line wrap
size_t b64_encoded_size(size_t inlen, size_t wrap);

//compute binary size required to store decoded base64 data
size_t b64_decoded_size(const char *in);

//encode binary to base64
//please remember to free the output
//wrap -- how many characters to insert a line wrap (\n) after
//by default this should be 76 according to RFC2045
char *b64_encode(const unsigned char *in, size_t len, size_t wrap);

//decode base64 to binary
//please remember to free up memory once done with output
//from b64_decoded_size function
//an additional byte is allocated at the end of the return pointer
//so if we want a string can append a \0 on the byte position using
//b64_decoded_size()
unsigned char *b64_decode(const char *in);

//check if it is a valid base64 alphabet
// ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
int b64_isvalidchar(char c);
