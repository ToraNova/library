/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular c wrapper source file
  April 17 2019

  developed by ToraNova
  chia_jason96@live.com
*/
#include "doubles.h"
#include "doubles.hpp"

using namespace arrayutil;

void arrayutil_doubles_libtest(){
	doubles::libtest();
	return;
}

double *arrayutil_doubles_array21join(double **source, size_t arow, size_t acol){
	return doubles::array21join(source, arow, acol);
}

double **arrayutil_doubles_array12split(double *source, size_t arow, size_t acol){
	return doubles::array12split(source, arow, acol);
}

void arrayutil_doubles_freedim(double **target, size_t arow){
	doubles::freedim(target, arow);
	return;
}

double **arrayutil_doubles_allocdim(size_t arow, size_t acol){
	return doubles::allocdim(arow,acol);
}

void arrayutil_doubles_split_vc(int sindex,double **source, size_t srow, size_t scol, double **spA, double **spB){
	doubles::split_vc(sindex,source,srow,scol,spA,spB);
	return;
}

void arrayutil_doubles_split_vcST(int sindex,double **source, size_t srow, size_t scol, double *spA, double *spB){
	doubles::split_vcST(sindex,source,srow,scol,spA,spB);
	return;
}

void arrayutil_doubles_split_vcSST(int sindex,double *source, size_t srow, size_t scol, double *spA, double *spB){
	doubles::split_vcSST(sindex,source,srow,scol,spA,spB);
	return;
}

void arrayutil_doubles_split_hc(int sindex,double **source, size_t srow, size_t scol, double **spA, double **spB){
	doubles::split_hc(sindex,source,srow,scol,spA,spB);
	return;
}

void arrayutil_doubles_split_hcST(int sindex,double **source, size_t srow, size_t scol, double *spA, double *spB){
	doubles::split_hcST(sindex,source,srow,scol,spA,spB);
	return;
}

void arrayutil_doubles_split_hcSST(int sindex,double *source, size_t srow, size_t scol, double *spA, double *spB){
	doubles::split_hcSST(sindex,source,srow,scol,spA,spB);
	return;
}

