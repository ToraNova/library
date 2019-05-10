/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular source file
  April 17 2019

  developed by ToraNova
  chia_jason96@live.com
*/
#include "doubles.hpp"

#include <iostream>
#include <string>

using namespace std;

namespace arrayutil{
namespace doubles{

	//library test
	void libtest(){
		cout<<"doubles_libtest OK"<<endl;
		return;
	}


	double *array21join(double **source, size_t arow, size_t acol){
		size_t i,j; //iterators

		//allocate for the long array
		double *out = (double *)malloc(sizeof(double)*arow*acol); 
		size_t k = 0; //long iterator
		for(i=0;i<arow;i++){
			for(j=0;j<acol;j++){
				out[k++] = source[i][j];
			}
		}
		return out;
	}

	double **array12split(double *source, size_t arow, size_t acol){
		size_t i,j; //iterators

		//allocate for the 2D array
		double **out = (double **)malloc(sizeof(double *)*arow); 
		size_t k = 0; //long iterator
		for(i=0;i<arow;i++){
			out[i] = (double *)malloc(sizeof(double)*acol);
			for(j=0;j<acol;j++){
				out[i][j] = source[k++];
			}
		}
		return out;
	}

	void freedim(double **target,size_t arow){
		size_t i; //array iterators

		for(i=0;i<arow;i++){
			free(target[i]);
		}
		free(target);
		return;
	}


	double **allocdim(size_t arow, size_t acol){
		size_t i; //array iterators
		
		double **out = (double **)malloc(sizeof(double *)*arow);
		for(i=0;i<arow;i++){
			out[i] = (double *)calloc(acol,sizeof(double));
		}
		return out;
	}

			

	void split_vc(int sindex,double **source, size_t srow, size_t scol, double **spA, double **spB){
		size_t i,j; //array iterators
		size_t ka=0,kb=0;

		for(i=0;i<scol;i++){
			if( i < sindex){
				//place into spA
				for(j=0;j<srow;j++){
					spA[j][ka] = source[j][i];
				}
				ka++;
			}else{
				for(j=0;j<srow;j++){
					spB[j][kb] = source[j][i];
				}
				kb++;
			}
		}
		return;
	}


	void split_vcST(int sindex,double **source, size_t srow, size_t scol, double *spA, double *spB){
		if(scol < sindex){
			log_err("split point larger than column size !");
			return;
		}
		size_t i,j;
		
		for(i=0;i<scol;i++){
			if( i < sindex){
				//place into spA
				for(j=0;j<srow;j++){
					spA[j*sindex+i] = source[j][i]; 
				}
			}else{
				for(j=0;j<srow;j++){
					spB[j*(scol-sindex)+i-sindex] = source[j][i];
				}
			}
		}
	}

	void split_vcSST(int sindex,double *source, size_t srow, size_t scol, double *spA, double *spB){
		if(scol < sindex){
			log_err("split point larger than column size !");
			return;
		}
		size_t i,j; //k is the long pointer for ST
		
		for(i=0;i<scol;i++){
			if( i < sindex){
				//place into spA
				for(j=0;j<srow;j++){
					spA[j*sindex+i] = source[j*scol+i]; 
				}
			}else{
				for(j=0;j<srow;j++){
					spB[j*(scol-sindex)+i-sindex] = source[j*scol+i];
				}
			}
		}
	}

	void split_hc(int sindex,double **source, size_t srow, size_t scol, double **spA, double **spB){
		size_t i,j; //array iterators
		size_t ka=0,kb=0;
		
		for(i=0;i<srow;i++){
			if( i < sindex){
				for(j=0;j<scol;j++){
					spA[ka][j] = source[i][j];
				}
				ka++;
			}else{
				for(j=0;j<scol;j++){
					spB[kb][j] = source[i][j];
				}
				kb++;
			}
		}
	}


	void split_hcST(int sindex,double **source, size_t srow, size_t scol, double *spA, double *spB){
		size_t i,j,ka=0,kb=0; //array iterators
		
		for(i=0;i<srow;i++){
			if( i < sindex){
				for(j=0;j<scol;j++){
					spA[ka++] = source[i][j];
				}
			}else{
				for(j=0;j<scol;j++){
					spB[kb++] = source[i][j];
				}
			}
		}
	}

	void split_hcSST(int sindex,double *source, size_t srow, size_t scol, double *spA, double *spB){
		size_t i,j,k=0;
		size_t ka=0,kb=0; //array iterators
		
		for(i=0;i<srow;i++){
			if( i < sindex){
				for(j=0;j<scol;j++){
					spA[ka++] = source[k++];
				}
			}else{
				for(j=0;j<scol;j++){
					spB[kb++] = source[k++];
				}
			}
		}
	}
}
}
