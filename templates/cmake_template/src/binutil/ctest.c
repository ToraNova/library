/*
	library C source file
	cmake_boostrap

	ToraNova 2019
*/

#include "torabinutil.h"

#ifdef __cplusplus
extern "C"{
#endif


#include <stdio.h>


void ctestfunc(){
  printf("Called from a c-source.\n");
  return;
}




#ifdef __cplusplus
};
#endif
