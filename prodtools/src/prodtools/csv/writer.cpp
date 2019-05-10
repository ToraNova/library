/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 22 2019

  @author ToraNova
  @version 1.2 April 22,2019
  @mailto chia_jason96@live.com
*/
#include "writer.hpp"

//standard libraries
#include <iostream>
#include <fstream> //for ifstreams
#include <sstream> //string streams
#include <cstdlib>

using namespace std;

namespace csvwriter

{

	//library test
	void libtest(){
		cout<<"csv_writer_libtest OK"<<endl;
		return;
	}


	bool writecsv_double(
			const char *filename,
			double **target,
			size_t arow,
			size_t acol,
			char delim
			)
	{
		size_t i,j;
		//creates the output file stream
		ofstream outfile;
		//opens the the file for output (overwrites)
		outfile.open(filename, ofstream::out);
		for(i=0;i<arow;i++){
			//perform row writing
			for(j=0;j<acol;j++){
				if(j+1==acol) outfile << target[i][j];
				else outfile << target[i][j] << delim;
			}
			outfile << endl;
		}
		return true;
	}
}
