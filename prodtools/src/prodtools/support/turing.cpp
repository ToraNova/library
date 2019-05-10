/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular source file
  April 17 2019

  developed by ToraNova
  chia_jason96@live.com
*/

/*
	turing.cpp - named in honor of Alan Turing
*/

#include "turegex.hpp"
#include <iostream>
#include <string>
#include <regex>

//in-house libraries
#include "convert.hpp"

using namespace std;

namespace turegex
{

	//library test
	void libtest(){
		cout<<"turegex_libtest OK"<<endl;
		return;
	}

	//fills the target buffer with double vals from real numbers
	//matched from the line 'input'. assumes target is already
	//allocated. set target to NULL if only want to count the
	//number of ocurrences
	size_t iter_double(const std::string& input, double *target){
		size_t i;
		//debug("iter_double input: %s",input.c_str());
		sregex_iterator iter = sregex_iterator( input.begin(),input.end(),real_number );
		if(target==NULL){
			//count the number of occurrences only
			for(i=0; iter != sregex_iterator(); i++){
				iter++; //only move forward on the iterations
			}
		}else{
			//record each occurrence
			for(i=0; iter != sregex_iterator(); i++){
				target[i] = suconv::string_double( iter++->str() );
			}
		}
		return i;
	}

}
