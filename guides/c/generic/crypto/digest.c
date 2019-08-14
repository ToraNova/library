/*
 * This code signs a message with a digest algo
 * with the cryptolib
 * gcc 9.1.0
 * gcc digest.c -o digest -lcrypto
 *
 * https://github.com/openssl/openssl/blob/master/doc/man3/EVP_DigestInit.pod
 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>

int main(int argc, char *argv[])
{
	//declared vars
	EVP_MD_CTX *mdctx;
	const EVP_MD *md;
	char defmsg[] = "Hello World";
	char *message;
	unsigned char md_value[EVP_MAX_MD_SIZE];
	unsigned int md_len, i;

	//usage parsing
	if (argv[1] == NULL) {
		printf("Usage: digest digestname message\n");
		exit(1);
	}

	if (argv[2] != NULL) {
		message = argv[2];
	}else{
		message = defmsg;
	}


	/*
	 * md5, sha1, sha224,
	 * sha256, sha512, mdc2
	 * ripemd160
	 */

	//initialization
	md = EVP_get_digestbyname(argv[1]);
	if (md == NULL) {
		printf("Unknown message digest %s\n", argv[1]);
		printf("md5, sha1, sha224, sha256, sha512, mdc2\n");
		printf("ripemd160\n");
		exit(1);
	}

	//digest (hashing)
	mdctx = EVP_MD_CTX_new();
	EVP_DigestInit_ex(mdctx, md, NULL);
	EVP_DigestUpdate(mdctx, message, strlen(message));
	EVP_DigestFinal_ex(mdctx, md_value, &md_len);
	EVP_MD_CTX_free(mdctx);

	//output
	for (i = 0; i < md_len; i++)
	printf("%02x", md_value[i]);
	printf("\n");

	exit(0);
}
