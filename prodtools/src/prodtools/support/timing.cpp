/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular C++ implementation file

  @author ToraNova
  @version 1.0 April 29,2019
  @mailto chia_jason96@live.com
*/
#include "timing.hpp"

#include <iostream>
#include <iomanip>
#include <string>
#include <ctime>
#include "sys/time.h"

//prodtools library includes
//it's ok for cpp files to use direct pathing
//since they're not directly used by other projects

using namespace std;

//TODO: Please edit the namespaces
namespace timing
{

	//library test
	void libtest(){
		cout<<"timing_libtest OK"<<endl;
		return;
	}

	void SimpleWallTimer::begin(){
		if(gettimeofday(&start,NULL)){
			log_err("Wall timer failed to gettimeofday when beginning");
		}
	}

	void SimpleWallTimer::end(){
		if(gettimeofday(&stop,NULL)){
			log_err("Wall timer failed to gettimeofday when ending");
		}
	}

	void SimpleWallTimer::print(){
		cout << "Wall Time (sec) :" << setprecision(10) << getdiff_secs() << endl;
	}

	double SimpleWallTimer::getdiff_secs(){
		return getstop_secs()-getstart_secs();
	}

	double SimpleWallTimer::getstart_secs(){
		return (double)start.tv_sec + (double)start.tv_usec * .000001;
	}

	double SimpleWallTimer::getstop_secs(){
		return (double)stop.tv_sec + (double)stop.tv_usec * .000001;
	}

	void SimpleCPUTimer::begin(){
		start = clock();
	}

	void SimpleCPUTimer::end(){
		stop = clock();
	}

	void SimpleCPUTimer::print(){
		cout << "CPU Time (sec) :" << setprecision(10) << getdiff_secs() << endl;
	}

	double SimpleCPUTimer::getdiff_secs(){
		return getdiff() / (double) CLOCKS_PER_SEC;
	}

	clock_t SimpleCPUTimer::getdiff(){
		return stop-start;
	}
}

