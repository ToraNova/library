/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular wrapper implementation file 

  @author ToraNova
  @version 1.0 April 18,2019
  @mailto chia_jason96@live.com
*/

#include "linear.hpp"
#include "linear.h"
	
//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
void linear_libtest(){
	linear::libtest();
	return;
}


/*
* Obtain a unity matrix of size dim
*/
double **linear_obtainUnity(size_t dim){
	return linear::obtainUnity(dim);
}

/*
* Obtain a unity matrix of size dim in 1D form
*/
double *linear_obtainUnityST(size_t dim){
	return linear::obtainUnityST(dim);
}
