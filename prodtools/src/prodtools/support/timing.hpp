/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular CPP main header file

  @author ToraNova
  @version 1.0 April 29,2019
  @mailto chia_jason96@live.com
*/

#ifndef TIMING_HPP
#define TIMING_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"
#include <ctime>

//NOTE : ALL INCLUDE FILES ARE RELATIVE FROM SRC
// prodtools/module_name/file

namespace timing
{

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void libtest();

	/*
	 * Attempts to measures interval
	 * For Posix/Linux systems only
	 */
	class SimpleWallTimer{
		protected:
		struct timeval start;
		struct timeval stop;

		public:
		void begin();
		void end();
		void print();
		double getdiff_secs();
		double getstart_secs();
		double getstop_secs();
	};
		

	/*
	 * Measures program time
	 * WARNING, this class measures CPU TIME.
	 * for multithreaded program, the time increases
	 * proportional to the number of threads
	 */
	class SimpleCPUTimer{
		protected:
		
		std::clock_t start;
		std::clock_t stop;

		public:
		/* skips the default constructor */

		void begin();
		void end();
		void print();
		double getdiff_secs();
		std::clock_t getdiff();
	};

};



#endif
