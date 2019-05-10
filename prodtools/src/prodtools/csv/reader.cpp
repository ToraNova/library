/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular source file
  April 16 2019

  developed by ToraNova
  chia_jason96@live.com
*/
#include "reader.hpp"

//standard libraries
#include <iostream>
#include <fstream> //for ifstreams
#include <sstream> //string streams
#include <cstdlib>

//prodtools library includes
#include "../support/convert.hpp"
#include "../support/suprint.hpp"
#include "../support/turegex.hpp"
#include "../arrayutil/all.hpp"

using namespace std;

namespace csvreader

{

	//library test
	void libtest(){
		cout<<"csv_reader_libtest OK"<<endl;
		return;
	}

	//default constructor
	DoubleReader::DoubleReader(){
		mrowcount = 0;
		mcolcount = 0;
	}

	//reads the named csv file returns 0 on success and 1 on fail
	//skipfirst indicates whether to skip the first line
	bool DoubleReader::readcsv(const char *filename,bool skipfirst){
		ifstream tmpfile = ifstream(filename,ifstream::in); //creates the filestream
		if(tmpfile.fail()){
			//failbit is set, return 1 for error
			log_err("Error occured when opening file %s",filename);
			return 1;
		}
		string line;
		uint32_t i;

		//obtain number of lines
	  for (mrowcount = 0 ; getline(tmpfile, line); mrowcount++) { }
		tmpfile.clear(); //clear the eof bit
		tmpfile.seekg(0,tmpfile.beg); //seek to head again

		if(skipfirst){
			mrowcount--;
			getline(tmpfile,line); //discards the first line again
		}
		debug("mrowcount :%zu",mrowcount); //debugging prints, comment out EDEBUG in ptdebug.h

		//get colcount on first entry
		getline(tmpfile,line);

		//perform a match on the line to obtain the no. of ocurrences, i.e colcount
		mcolcount = turegex::iter_double(line, NULL);
		debug("mcolcount :%zu",mcolcount); //debugging prints, comment out EDEBUG in ptdebug.h

		//reset
		tmpfile.clear();
		tmpfile.seekg(0,tmpfile.beg); //seek to head again
		if(skipfirst)getline(tmpfile,line); //discards the first line again

		//allocates the main memory
		mdouble = (double **) malloc(sizeof(double *)*mrowcount);
		for(i = 0 ;i<mrowcount && getline(tmpfile,line);i++){
		//allocate memory
			mdouble[i] = (double *)malloc(sizeof(double)*mcolcount);
			//reads the line by matching real numbers, stores into the ith row
			turegex::iter_double(line, mdouble[i]);
		}
		tmpfile.close();
		return 0;
	}
	
	//'borrow' the mdouble pointer
	double **DoubleReader::borrow_mdouble(){
		return mdouble;
	}

	//show array
	void DoubleReader::show_mdouble(){
		suprint::doublearr2D(mdouble, mrowcount, mcolcount);
	}

	//destructor - free all memories
	void DoubleReader::freeall(){
		arrayutil::doubles::freedim(mdouble,mrowcount);
	}

	//perform splitting on the mdouble for preallocated spA and spB
	//allocation of spA and spB is the caller's responsibility
	//s/he is also in charge of freeing spA and spB
	bool DoubleReader::split_mdouble_vc(int sindex, double **spA, double **spB){
		if(sindex >= mcolcount){
			log_info("Warning sindex >= mcolcount. intended ?");
		}
		arrayutil::doubles::split_vc(sindex, mdouble, mrowcount, mcolcount, spA, spB);
		return true;
	}

	//perform splitting on the mdouble for preallocated spA and spB
	//allocation of spA and spB is the caller's responsibility
	//s/he is also in charge of freeing spA and spB
	bool DoubleReader::split_mdouble_vcST(int sindex, double *spA, double *spB){
		if(sindex >= mcolcount){
			//input sanitation (minimal)
			log_info("Warning sindex >= mcolcount. intended ?");
		}
		arrayutil::doubles::split_vcST(sindex, mdouble, mrowcount, mcolcount, spA, spB);
		return true;
	}

	//perform splitting on the mdouble for preallocated spA and spB
	//allocation of spA and spB is the caller's responsibility
	//s/he is also in charge of freeing spA and spB
	bool DoubleReader::split_mdouble_hc(int sindex, double **spA, double **spB){
		if(sindex >= mrowcount){
			//input sanitation (minimal)
			log_info("Warning sindex >= mrowcount. intended ?");
		}
		arrayutil::doubles::split_hc(sindex, mdouble, mrowcount, mcolcount, spA, spB);
		return true;
	}

	//perform splitting on the mdouble for preallocated spA and spB
	//allocation of spA and spB is the caller's responsibility
	//s/he is also in charge of freeing spA and spB
	bool DoubleReader::split_mdouble_hcST(int sindex, double *spA, double *spB){
		if(sindex >= mrowcount){
			//input sanitation (minimal)
			log_info("Warning sindex >= mrowcount. intended ?");
		}
		arrayutil::doubles::split_hcST(sindex,mdouble,mrowcount, mcolcount, spA, spB);
		return true;
	}
}
