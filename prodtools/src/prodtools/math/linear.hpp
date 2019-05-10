/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file

  @author ToraNova
  @version 1.0 April 18,2019
  @mailto chia_jason96@live.com
*/

#ifndef LINEAR_HPP
#define LINEAR_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"

//NOTE : ALL INCLUDE FILES ARE RELATIVE FROM SRC
// prodtools/module_name/file

namespace linear
{

  //Convention : Each library comes with a libtester <module_name>_<part>_libtest()
  void libtest();


  /*
   * Obtain a unity matrix of size dim
   */
  double **obtainUnity(size_t dim);

  /*
   * Obtain a unity matrix represented as a 1D array (ST form)
   */
  double *obtainUnityST(size_t dim);
}

#endif
