/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header wrapper file 

  @author ToraNova
  @version 1.0 April 18,2019
  @mailto chia_jason96@live.com
*/

#ifndef LINEAR_H
#define LINEAR_H

#include <string.h>
#include <stdint.h>

//NOTE : ALL INCLUDE FILES ARE RELATIVE FROM SRC
// prodtools/module_name/file

#ifdef __cplusplus
extern "C"{
#endif

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void linear_libtest();


	/*
	* Obtain a unity matrix of size dim
	*/
	double **linear_obtainUnity(size_t dim);

	/*
	 * obtain a 1D representation of a 2D unity matrix
	 */
	double *linear_obtainUnityST(size_t);


#ifdef __cplusplus
}
#endif

#endif
