
/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 16 2019

  developed by ToraNova
  chia_jason96@live.com
*/

#ifndef DOUBLES_HPP
#define DOUBLES_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"

namespace arrayutil{
namespace doubles{

	void libtest();

	/*
	* joins a 2D array into a serial 1D array,
	* place the ptr to the 1D array in dest,
	* while source is the 2D array
	* returns the pointer to the 1D array (ST form)
	* basiclaly converts a 2D array to ST forms
	*/
	double *array21join(double **source, size_t arow, size_t acol);

	/*
	* splits a 1D array into a 2D array,
	* returns the pointer to the 2D array
	* note that acol * arow is also the expected size of the source array
	*/
	double **array12split(double *source, size_t arow, size_t acol);

	/*
	* Frees up a 2D pointer
	*/
	void freedim(double **target, size_t arow);

	/*
	 * Performs a dimensional allocation for a 2D pointer
	 */
	double **allocdim(size_t arow, size_t acol);

	/*
	 * Splits the source matrix with a vertical cut
	 * spA and spB should be allocated outside respectively
	 * before being passed into this function
	 * spA and spB should have the same amount of rows
	 * sindex represents the cutting point.
	 * if sindex == 0, no split has ocurred, spB equivalent to source
	 * if sindex == mcolcount of source, no split has ocurred, spA equivalent to source
	 * if sindex == N where N is between 0 and mcolcount of source,
	 * then the Nth col goes to B while any col before N goes to A
	 * e.g, if N == 1, then spB gets column 1,2,3,4
	 * while spA gets column 0
	 * srow and scol and the row size and col size of the source array
	*/
	void split_vc(int sindex,double **source, size_t srow, size_t scol, double **spA, double **spB);

	/*
	 * similar to split_vc but splits are in ST form
	 * ST form indicate a 2D array represented by 1D pointer structurally
	 */
	void split_vcST(int sindex,double **source, size_t srow, size_t scol, double *spA, double *spB);

	/*
	 * similar to split_vc but source and splits are in ST form
	 */
	void split_vcSST(int sindex,double *source, size_t srow, size_t scol, double *spA, double *spB);

	/*
	 * Splits the source matrix with a vertical cut
	 * spA and spB should be allocated outside respectively
	 * before being passed into this function
	 * spA and spB should have the same amount of columns
	 * sindex represents the cutting point.
	 * if sindex == 0, no split has ocurred, spB equivalent to source
	 * if sindex == mrowcount of source, no split has ocurred, spA equivalent to source
	 * if sindex == N where N is between 0 and mrowcount of source,
	 * then the Nth row goes to B while any row before N goes to A
	 * e.g, if N == 1, then spB gets rows 1,2,3,4
	 * while spA gets row 0
	 * srow and scol and the row size and col size of the source array
	*/
	void split_hc(int sindex,double **source, size_t srow, size_t scol, double **spA, double **spB);


	/*
	 * similar to split_hc but splits are in ST form
	 * ST form indicate a 2D array represented by 1D pointer structurally
	 */
	void split_hcST(int sindex,double **source, size_t srow, size_t scol, double *spA, double *spB);

	/*
	 * similar to split_hc but source and splits are in ST form
	 */
	void split_hcSST(int sindex,double *source, size_t srow, size_t scol, double *spA, double *spB);
}
}

#endif
