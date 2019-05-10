/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular C wrapper header file

  @author ToraNova
  @version 1.0 April 16,2019
  @mailto chia_jason96@live.com
*/

#ifndef TEMPLATE_H
#define TEMPLATE_H

//C system headers
#include<stdint.h>
#include<string.h>

//NOTE : ALL INCLUDE FILES ARE RELATIVE FROM SRC
// prodtools/module_name/file

//prevents g++ from mangling the header
#ifdef __cplusplus
extern "C" {
#endif

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void template_libtest();

#ifdef __cplusplus
}
#endif

#endif
