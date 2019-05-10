/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 22 2019

  @author ToraNova
  @version 1.2 April 22,2019
  @mailto chia_jason96@live.com
*/

#ifndef WRITER_H
#define WRITER_H

#include <stdint.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif

void csvwriter_libtest();

//attempts to write a double array to a csv file, returns true upon success.
int csvwriter_writecsv_double(const char *filename,double **target, size_t arow, size_t acol, char delim);

#ifdef __cplusplus
};
#endif

#endif
