/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 22 2019

  @author ToraNova
  @version 1.2 April 22,2019
  @mailto chia_jason96@live.com
*/

#ifndef WRITER_HPP
#define WRITER_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"

namespace csvwriter

{

  void libtest();
  //attempts to write a double array to a csv file, returns true upon success.
  bool writecsv_double(const char *filename,double **target, size_t arow, size_t acol, char delim);

}

#endif
