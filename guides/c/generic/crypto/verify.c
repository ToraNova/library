/*
 * Verifies a digest (Digest and verifies are done separately)
 * ToraNova 2019 aug 14
 * gcc 9.1.0
 * gcc sign.c -o sign -lcrypto
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>
#include <openssl/pem.h>

int main(int argc, char *argv[]){

	//declare vars
	EVP_PKEY *pkey = NULL;
	EVP_MD_CTX *mdctx = EVP_MD_CTX_create();
	const EVP_MD *md = EVP_sha512(); //sha512

	//result codes
	int rc;
	unsigned int d_size, i;
	size_t s_size;
	unsigned char d_message[EVP_MAX_MD_SIZE];
	unsigned char s_message[EVP_MAX_MD_SIZE];
	FILE *sigf, *pubf;
	unsigned char tmp;

	//target message
	char message[] = "Hello World";

	//open file stream
	if(argc < 3){
		printf("Please specify the public key file and the signature file.\n");
		printf("verify <public> <signature>\n");
		exit(1);
	}else{
		pubf = fopen( argv[1], "r" );
		sigf = fopen( argv[2], "r" );
	}

	//reads the public key for verifying
	pkey = PEM_read_PUBKEY( pubf, &pkey , NULL, NULL);
	if( pkey == NULL )printf("Invalid public key\n");

	//reads the signature file to obtain the sig, stores into s_message
	s_size = 0;
	while( fscanf(sigf, "%02x", &tmp) >= 1 ){
		s_message[s_size] = tmp; //place into buffer
		s_size++;
	}

	//output
	printf("Verifying signature of size %zu on: ",s_size);
	for (i = 0; i < s_size; i++){
		printf("%02x", s_message[i]);
	}
	printf("\n");

	//hashing the message, output in d_message with size d_size
	rc = EVP_Digest( message, strlen(message), d_message, &d_size, md, NULL);

	//initialize the verifying
	rc = EVP_DigestVerifyInit(mdctx, NULL, NULL, NULL, pkey);

	//verification
	rc = EVP_DigestVerify(mdctx, s_message, s_size, d_message, d_size);

	if(rc == 1){
		//success
		printf("OK\n");
	}else{
		//fail
		printf("FAIL\n");
	}

	fclose(sigf);
	fclose(pubf);
	EVP_MD_CTX_free(mdctx);
}
