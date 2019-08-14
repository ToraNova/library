#include <stdlib.h>

//defines
int expo(int base,int exp){
	//integer only. returns base raised to power of exp
	int out = 1;
	while(exp--){
		out *= base;
	}
	return out;
}

unsigned long expol(int base,int exp){
	//integer only. returns base raised to power of exp
	unsigned long out = 1;
	while(exp--){
		out *= base;
	}
	return out;
}

int* genPrimeArr(int n){
	if(n<2){n = 2;}//n should be 2 by minimum
	//int *out = calloc(n,sizeof(int));
	int *out = malloc((n+1)*sizeof(int));
	//alternatively with malloc
	// (int *)malloc(n*sizeof(int));
	out[0] = 2;
	out[1] = 3;

	n=n-2;
	int i = 1; int j,k;	
	int notPrime;
	while(n>=0){
		
		for(j=out[i]+1;;j++){
			notPrime = 0;//possible prime
			for(k=0;k<i;k++){
				if(j % out[k] ==0){
					//not a prime
					notPrime =1;
					break;
				}
			}
			if(! notPrime){
				out[++i] = j; //new prime
				break;
			}
		}	
		n--;
	}
	return out;
}

int relativePrime(int a,int b){
	//checks if a is relatively prime to b
	//a < b
	int temp;
	if(a>b){
		temp = a;
		a = b;
		b = temp;
	}else if(a==b){
		//since a==b, they both must share the same factors other than 1,they
		//are not relatively prime
		return 0;
	}
	
	int i;
	for(i=2;i<b;i++){
		//check if i can divide both A and B
		if(a % i == 0 && b % i == 0){
			return 0; //not relatively prime
		}
	}
	return 1;//they are relatively prime as nothing other than 1 divides both a and b
}
	


	

