/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular source file
  April 18 2019

  developed by ToraNova
  chia_jason96@live.com
*/

#include "linear.hpp"
#include <iostream>

using namespace std;

//TODO: Please edit the namespaces
namespace linear
{

	//library test
	void libtest(){
		cout<<"linear_libtest OK"<<endl;
		return;
	}


	double **obtainUnity(size_t dim){
		size_t i; //iterator
		double **out = (double **)malloc(sizeof(double *)*dim);
		for(i=0;i<dim;i++){
			out[i] = (double *)calloc(dim,sizeof(double));
			out[i][i] = 1; //leading element
		}
		return out;
	}	

	//ST form of a unity matrix 2D matrix structured as a single dbl pointer
	//to reduce pointer complexity
	double *obtainUnityST(size_t dim){
		size_t i; //iterator
		double *out = (double *)calloc(dim*dim,sizeof(double ));
		for(i=0;i<dim;i++){
			out[i+i*dim] = 1; //leading element
		}
		return out;
	}	
}
