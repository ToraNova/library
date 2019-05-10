/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 16 2019

  developed by ToraNova
  chia_jason96@live.com
*/

#ifndef CONVERT_HPP
#define CONVERT_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"


//support conversion namespace suconv
namespace suconv{

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void libtest();

	double string_double(const std::string& s);
}





#endif
