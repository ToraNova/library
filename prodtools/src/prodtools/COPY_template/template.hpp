/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular CPP main header file

  @author ToraNova
  @version 1.0 April 16,2019
  @mailto chia_jason96@live.com
*/

#ifndef TEMPLATE_HPP
#define TEMPLATE_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"

//NOTE : ALL INCLUDE FILES ARE RELATIVE FROM SRC
// prodtools/module_name/file

namespace template
{

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void libtest();

	//Convention : Classnames are capitalized
	class SomeCustomClass(){
	//comments should always be on top
	//private members/protected member attr must start with m

	};

}



#endif
