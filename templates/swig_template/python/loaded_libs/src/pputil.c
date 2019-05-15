/*
 * PyPLASMA utility functions
 * For utility such as file loading/reading
 * and other auxiliaries
 */

/*
 * include the irrelevant header
 */
#include "../include/pputil.h"
#include "../include/irr.h"

/*
 * standard libraries
 */
#include <assert.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <omp.h>

/*
 *	PRODTOOLS includes
 */
#include <prodtools/arrayutil/doubles.h>
#include <prodtools/math/linear.h>
#include <prodtools/support/timing.h>
#include <prodtools/support/suprint.h>

/*
 *	PLASMA CORE BLAS includes
 */
#include "core_lapack.h"
#include "core_blas.h"
#include "plasma.h"

#define REAL

/*
 * PLASMA library docs from doxygen
 * http://icl.bitbucket.io/plasma/
 */

/*
 * library test function. to check if everything is OK
 */
void pputil_test(){
	printf("pputil OK\n");
	//test if arrayutil is actually working
	arrayutil_doubles_libtest();
	linear_libtest();
	return;
}

/*
 * perform Ridge Regression on the input Dmat
 * and Tvct. they're both 1D representation
 * of the double array, thus, please specify also
 * their dimensions
 * @params Dmat - input Data matrix to perform ridge regression on
 * @params Tvct - input Target vector to train on
 * @params xrowsz, xcolsz - the rowsize, colsize of Dmat
 * @params yelmsz, ydimsz - the rowsize, colsize of Tvct
 *
 * this function is now stable. please refrain from editing 10th May 19 - ToraNova
 */
double *pputil_ridge(
	double *Dmat, size_t xrowsz, size_t xcolsz,
	double *Tvct, size_t yelmsz, size_t ydimsz,
	double lambda
){
	//var declares
	double *alpha, *symmetricL; //intermediaries
	int rc; //used to store result codes

	//current assumption, ydimsz == 1
	if(ydimsz > 1)log_err("Warning: untested code for target dim > 1");
	
	//obtain unity matrix
	symmetricL = linear_obtainUnityST( yelmsz );
	debug("Unity obtained (size:%ld)",yelmsz);

	//allocate memory for alpha 
	alpha  = (double *)calloc( xrowsz* ydimsz, sizeof(double));
	debug("alpha array created (%ld/%ld)",xrowsz,ydimsz);

#ifdef EDEBUG
	//declares the weight array (for debugging only)
	double *weight;
	weight = (double *)calloc( xcolsz* ydimsz, sizeof(double));
	debug("weight array allocated (%ld/%ld)",ydimsz,xcolsz);
	//timing mechanism
	timing_SimpleWallTimer *stimer = constr_SimpleWallTimer();
	SimpleWallTimer_begin(stimer);
#endif

	//begin plasma
	plasma_init();
	debug("Starting pputil_ridge with lambda %1.3f",lambda);

	//this performs XtX on row major data
	rc = plasma_dsyrk(
		PlasmaLower, PlasmaTrans,
		yelmsz, xcolsz,
		1.0, Dmat, xcolsz,
		lambda, symmetricL, yelmsz);
	debug("plasma_dsyrk routine complete. %d",rc);

	//perform cholesky's decomposition
	rc = plasma_dpotrf(PlasmaLower, yelmsz, symmetricL, yelmsz);
	debug("plasma_dpotrf routine complete. %d",rc);

	//now perform the inversion
	rc = plasma_dpotri(PlasmaLower, yelmsz, symmetricL, yelmsz);
	debug("plasma_dpotri routine complete. %d",rc);

	/*
	 * ASSERTION - inversion is OK
	 */

	//recover the alpha to prepare for redistribution
	rc = plasma_dsymm(
		PlasmaLeft, PlasmaLower,
		xrowsz, ydimsz, lambda,
		symmetricL, yelmsz,
		Tvct, xrowsz,
		0.0, alpha, xrowsz);
	debug("plasma_dsymm routine complete. %d",rc);


	//these steps are not actually required in actual practice
	//only used for debugging
#ifdef EDEBUG
	//prints the alpha out
	//not really necessary since alphas can be very large
	//suprint_doublearrST(alpha, ydimsz, xrowsz, 14, 5);

	//this step is not actually required in actual practice
	//only used for debuggin
	rc = plasma_dgemm(
		PlasmaNoTrans, PlasmaNoTrans,
		xcolsz, ydimsz, xrowsz,
		1.0, Dmat, xcolsz,
		     alpha, xrowsz,
		0.0, weight, xcolsz);
	debug("plasma_dgemm routine complete. %d",rc);
	debug("Test weights obtained.");
	//prints the weights out
	suprint_doublearrST(weight, ydimsz, xcolsz, 14, 5);

	//timer and array cleanup
	SimpleWallTimer_end(stimer);
	SimpleWallTimer_print(stimer);
	destr_SimpleWallTimer(stimer);
	free(weight);
#endif

	plasma_finalize();
	free(symmetricL);
	return alpha;
}


	
