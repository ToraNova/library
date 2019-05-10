/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular c wrapper source file
  April 17 2019

  developed by ToraNova
  chia_jason96@live.com
*/

#include "suprint.hpp"
#include "suprint.h"

//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
void suprint_libtest(){
	suprint::libtest();
	return;
}

//prints a char repetitively
void suprint_repeatchar(char target, unsigned int repeats, int newline){
	suprint::repeatchar(target,repeats,newline);
	return;
}

//double array printers
void suprint_doublearr(double *target, size_t asize, int width, int precision){
	suprint::doublearr(target,asize,width,precision);
	return;
}

//print a 2D double array
void suprint_doublearr2D(double **target, size_t arow, size_t acol, int width, int precision){
	suprint::doublearr2D(target,arow,acol,width,precision);
	return;
}

void suprint_doublearrST(double *target, size_t arow, size_t acol, int width, int precision){
	suprint::doublearrST(target,arow,acol,width,precision);
	return;
}

//similar to doublearr, but no width and precision setting
void suprint_pdoublearr(double *target,size_t asize){
	suprint::pdoublearr(target,asize);
	return;
}

