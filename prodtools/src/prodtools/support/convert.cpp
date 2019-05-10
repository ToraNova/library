/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular source file
  April 17 2019

  developed by ToraNova
  chia_jason96@live.com
*/
#include "convert.hpp"

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

namespace suconv
{

  //library test
  void libtest(){
  	cout<<"convert_libtest OK"<<endl;
  	return;
  }

  double string_double(const std::string& s){
  	//original author : Alessandro Jacopson
  	//from stackoverflow
  	istringstream i(s); //form the stream
     double x;
     if (!(i >> x)){
  		 //error has occurred
  		 log_info("Conversion error on string_double");
  		 return 0;
  	 }
     return x;
  }

}
