/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular source file
  April 16 2019

  developed by ToraNova
  chia_jason96@live.com
*/
#include "suprint.hpp"
#include "../arrayutil/all.hpp"

#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

namespace suprint
{

	//library test
	void libtest(){
		cout<<"print_libtest OK"<<endl;
		return;
	}
	
	//for printing beautification
	void repeatchar(char target, unsigned int repeats, bool newline){
		unsigned int r;//counter
		for(r = 0;r < repeats; r++){
			cout << target;
		}
		if(newline) cout << endl;
	}

	//print a double array by a for loop iter
	void doublearr(
		double *target,
		size_t asize,
		int width,
		int precision
	)
	{
		uint32_t i;
		for(i=0;i<asize;i++){
			cout << setw(width) << setprecision(precision) << target[i];
		}
		cout << endl;
		return;
	}

	void doublearrST(
		double *target,
		size_t arow,
		size_t acol,
		int width,
		int precision
		)
	{
		size_t i,j,k;
		k=0; //initialize long counter
		for(i=0;i<arow;i++){
			for(j=0;j<acol;j++){
				cout << setw(width) << setprecision(precision) << target[k++];
			}
			cout << endl;
		}
		return;
	}

	void pdoublearr(
		double *target,
		size_t asize
	)
	{
		uint32_t i;
		for(i=0;i<asize;i++){
			cout << target[i] << ' ';
		}
		cout << endl;
		return;
	}

	//print a 2D array
	void doublearr2D(
		double **target,
		size_t arow,
		size_t acol,
		int width,
		int precision
	)
	{
		uint32_t i;
		for(i=0;i<arow;i++){
			doublearr(target[i],acol,width,precision);
		}
		return;
	}

}
