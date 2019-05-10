/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular C wrapper header file

  @author ToraNova
  @version 1.0 April 29,2019
  @mailto chia_jason96@live.com
*/

#ifndef TIMING_H
#define TIMING_H

//C system headers
#include<stdint.h>
#include<string.h>
#include<time.h>

//NOTE : ALL INCLUDE FILES ARE RELATIVE FROM SRC
// prodtools/module_name/file

typedef struct timing_SimpleCPUTimer timing_SimpleCPUTimer;
typedef struct timing_SimpleWallTimer timing_SimpleWallTimer;

//prevents g++ from mangling the header
#ifdef __cplusplus
extern "C" {
#endif

	//Convention : Each library comes with a libtester <module_name>_<part>_libtest()
	void timing_libtest();

	/*
	 * Attempts to measures interval
	 * For Posix/Linux systems only
	 */
	timing_SimpleWallTimer *constr_SimpleWallTimer();
	void SimpleWallTimer_begin(timing_SimpleWallTimer *cptr);
	void SimpleWallTimer_end(timing_SimpleWallTimer *cptr);
	void SimpleWallTimer_print(timing_SimpleWallTimer *cptr);
	double SimpleWallTimer_getstart_secs(timing_SimpleWallTimer *cptr);
	double SimpleWallTimer_getstop_secs(timing_SimpleWallTimer *cptr);
	double SimpleWallTimer_getdiff_secs(timing_SimpleWallTimer *cptr);
	void destr_SimpleWallTimer( timing_SimpleWallTimer *cptr);

	/*
	 * Measures program time
	 * WARNING, the following routines measures CPU TIME.
	 * for multithreaded program, the time increases
	 * proportional to the number of threads
	 */
	timing_SimpleCPUTimer *constr_SimpleCPUTimer();
	void SimpleCPUTimer_begin(timing_SimpleCPUTimer *cptr);
	void SimpleCPUTimer_end(timing_SimpleCPUTimer *cptr);
	void SimpleCPUTimer_print(timing_SimpleCPUTimer *cptr);
	double SimpleCPUTimer_getdiff_secs(timing_SimpleCPUTimer *cptr);
	clock_t SimpleCPUTimer_getdiff(timing_SimpleCPUTimer *cptr);
	void destr_SimpleCPUTimer( timing_SimpleCPUTimer *cptr);



#ifdef __cplusplus
}
#endif

#endif
