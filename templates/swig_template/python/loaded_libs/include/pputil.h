/*
 * PyPLASMA utility functions
 * for utility such as file loading/reading
 * unity generations and others
 */

#ifndef PPUTIL_H
#define PPUTIL_H

#include <stdint.h>
#include <stddef.h>

/*
 * Test function to ensure library usability
 */
void pputil_test();

double *pputil_ridge(
	double *Dmat, size_t xrowsz, size_t xcolsz,
	double *Tvct, size_t yelmsz, size_t ydimsz,
	double lambda
);

#endif
