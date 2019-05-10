/*
 * Irrelevant to plasma
 * This file is to test use on swig
 * and to create a sample wrapper
 */

#include <stdio.h>

//include the irrelevant header
#include "../include/irr.h"
//#include "irr.h"

void test(){
        //test printing
	printf("Wrapper Test OK\n");
	return;
}

void argtest(int arg1){
        //test argument passing
	printf("Wrapper Arg Test OK :%d\n",arg1);
	return;
}

