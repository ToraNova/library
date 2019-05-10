/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file

  @author ToraNova
  @version 1.1 April 18,2019
  @mailto chia_jason96@live.com
*/

#ifndef SUPRINT_HPP
#define SUPRINT_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"


//the support printing namespace, suprint
namespace suprint
{

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void libtest();

	//print a character repetitively. newline to insert endl at end of prints
	void repeatchar(char target, unsigned int repeats, bool newline);

	//double array printers
	void doublearr(double *target, size_t asize, int width=8, int precision=4);
	//print a 2D double array
	void doublearr2D(double **target, size_t arow, size_t acol, int width=8, int precision=4);
	//print a 1D array as a 2D (used when splitting)
	//this function is not ideal, please use it only for debugging.
	void doublearrST(double *target, size_t arow, size_t acol, int width=8, int precision=4);

	//similar to doublearr, but no width and precision setting
	void pdoublearr(double *target,size_t asize);

}

#endif
