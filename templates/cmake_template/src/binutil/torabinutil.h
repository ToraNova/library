/*
	library header file
	cmake_boostrap

	ToraNova 2019
*/

#ifndef TORABINUTIL_H
#define TORABINUTIL_H

//library test
void binlibtest();
void hexlibtest();


//extern "C" basically instructs the compiler
//to not perform name mangling on the definitions
//compat test
#ifdef __cplusplus
extern "C"{
#endif

//c declarations here
void ctestfunc();

#ifdef __cplusplus
};
#endif


#endif
