/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 17 2019

  developed by ToraNova
  chia_jason96@live.com
*/

#ifndef TUREGEX_HPP
#define TUREGEX_HPP

#define REAL_NUMBER_REGEX "[0-9]+(\\.[0-9]*((e|E)(\\+|-)[0-9]+)?)?"

//standard header includes
#include "prodtools/ptmodheaders.hpp"

#include <regex>

namespace turegex
{

	//only created once.
	const std::regex real_number(REAL_NUMBER_REGEX);

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void libtest();

	//set target==NULL to only count, returns size_t
	size_t iter_double( const std::string& input, double *target = NULL );

}

#endif
