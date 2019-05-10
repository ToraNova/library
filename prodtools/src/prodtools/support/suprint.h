/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 16 2019

  developed by ToraNova
  chia_jason96@live.com
*/

#ifndef SUPRINT_H
#define SUPRINT_H

#include<stdint.h>
#include<string.h>

#ifdef __cplusplus
extern "C" {
#endif

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void suprint_libtest();

	//print repetitively - refer to original hpp description
	void suprint_repeatchar(char target, unsigned int repeats, int newline);

	//double array printers
	void suprint_doublearr(double *target, size_t asize, int width, int precision);

	//print a 2D double array
	void suprint_doublearr2D(double **target, size_t arow, size_t acol, int width, int precision);

	//print a 1D array as a 2D structure
	void suprint_doublearrST(double *target, size_t arow, size_t acol, int width, int precision);

	//similar to doublearr, but no width and precision setting
	void suprint_pdoublearr(double *target,size_t asize);

#ifdef __cplusplus
};
#endif


#endif
