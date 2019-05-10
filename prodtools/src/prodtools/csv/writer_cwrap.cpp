/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular C wrapper file
  April 22 2019

  @author ToraNova
  @version 1.2 April 22,2019
  @mailto chia_jason96@live.com
*/
#include "writer.hpp"
#include "writer.h"

void csvwriter_libtest(){
	csvwriter::libtest();
  return;
}

//attempts to write a double array to a csv file, returns true upon success.
int csvwriter_writecsv_double(const char *filename,double **target, size_t arow, size_t acol, char delim){
	return csvwriter::writecsv_double(filename,target,arow,acol,delim);
}
