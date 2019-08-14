/*
 * This file generates a Ed25519 key and prints it on STDOUT/file
 * the public key is printed onto the std output
 * requires openssl 1.1.1 for ed25519
 * compile with :
 * gcc 9.1.0
 * gcc ed25519key.c -o ed25519gen -lcrypto
 *
 * reference:
 * https://github.com/openssl/openssl/blob/master/doc/man7/ed25519.pod
 */

#include<stdio.h>
#include<stdlib.h>
#include <openssl/evp.h>
#include <openssl/pem.h>

//usage:
//ed25519gen private > public
//writes private key to file 'private' and public key to file 'public'
int main(int argc, char *argv[]){

	FILE *streamctl;
	uint8_t b;

	if( argc < 2){
		//if no args, then print to stdout
		streamctl = stdout;
		b=0;
	}else{
		//else, print to a filestream
		streamctl = fopen(argv[1], "w");
		b=1;
	}

	EVP_PKEY *pkey = NULL;
	EVP_PKEY_CTX *pctx = EVP_PKEY_CTX_new_id(EVP_PKEY_ED25519, NULL);
	EVP_PKEY_keygen_init(pctx);
	EVP_PKEY_keygen(pctx, &pkey);
	EVP_PKEY_CTX_free(pctx);
	PEM_write_PrivateKey(streamctl, pkey, NULL, NULL, 0, NULL, NULL);
	PEM_write_PUBKEY(stdout, pkey);

	fclose(streamctl);
	return 0;
}
