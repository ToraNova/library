/*
 *
 *	C_run : A test run program
 *	to try and run the intended
 *	python wrapping target in C
 *	first.
 *
 * 	ToraNova 2019
 */

#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <omp.h>

#include "core_lapack.h"
#include "core_blas.h"
#include "plasma.h"

#include "../include/irr.h"
#include "../include/pputil.h"

//prodtools
#include "prodtools/csv/reader.h"
#include "prodtools/support/suprint.h"


int main(int argc, char *argv[]){
	/*
	 * main driver program
	 */

	//var declares
	double lambda = 1.0;
	double *alpha;
	double *yvct;
	double *xmat;

	size_t xrowsz, xcolsz, yelmsz, ydimsz;
	size_t rrow, rcol;
	int rc;

	//reader
	csvreader_DoubleReader *mr = constr_DoubleReader();
	rc = DoubleReader_readcsv(mr, "/home/cjason/library/python/pysample/datagen/data0.csv",0);
	debug("Read RC:%d",rc);
	rrow = DoubleReader_getRowCount(mr);
	rcol = DoubleReader_getColCount(mr);
	//no. of features on the y vector
	ydimsz = 1;
	xcolsz = rcol-ydimsz;
        xrowsz = rrow;	
	yelmsz = rrow;
	xmat = (double *)calloc( xrowsz* xcolsz, sizeof(double));
      	yvct = (double *)calloc( ydimsz* yelmsz, sizeof(double));	

	DoubleReader_split_mdouble_vcST(mr, xcolsz, xmat, yvct);
	debug("Splitting via rows as data entires");

	//real test
	alpha = pputil_ridge( 
			xmat, xrowsz, xcolsz,
			yvct, yelmsz, ydimsz,
			lambda);
	//cleanup
	destr_DoubleReader(mr);
	free(alpha);
	free(yvct);
	free(xmat);

	return 0;
}
