/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 16 2019

  @author ToraNova
  @version 1.2 April 16,2019
  @mailto chia_jason96@live.com
*/

#ifndef READER_HPP
#define READER_HPP

//standard header includes
#include "prodtools/ptmodheaders.hpp"

namespace csvreader

{

	void libtest();


	class DoubleReader {

		protected:
		//internal array
		double **mdouble;

		//stores the row and col count
		size_t mrowcount;
		size_t mcolcount;

		public:
		/*
		Default constructor
		*/
		DoubleReader();

		/*
		Reads a csv file, storing the read contents into mdouble
		sets skipfirst to true to skip the first row
		*/
		bool readcsv(const char *filename, bool skipfirst=false);

		/* 'borrows' the mdouble pointer. the user MUST not under any circumstances
		* free it
		*/
		double **borrow_mdouble();

		/*
		 * Refer to arrayutil.hpp for functional description
		 */
		bool split_mdouble_vc(int sindex, double **spA,  double **spB);

		/*
		 * Similar to the above function, except ST form is used,
		 * that is, a singular double pointer is used to represent
		 * a structured 2D matrix
		 */
		bool split_mdouble_vcST(int sindex, double *spA,  double *spB);

		/*
		 * Splits the mdouble matrix with a horizontal cut
		 * spA and spB should be allocated outside respectively
		 * before being passed into split_mdouble
		 * spA and spB will have the same amount of columns
		 * sindex represents the cutting point.
		 * if sindex == 0, no split has ocurred, spB equivalent to mdouble
		 * if sindex == mrowcount, no split has ocurred, spA equivalent to mdouble
		 * if sindex == N where N is between 0 and mrowcount,
		 * then the Nth row goes to B while any row before N goes to A
		 * e.g, if N == 1, then spB gets rows 1,2,3,4
		 * while spA gets row 0
		*/
		bool split_mdouble_hc(int sindex, double **p1, double **p2);


		/*
		 * Similar to the above function, except ST form is used,
		 * that is, a singular double pointer is used to represent
		 * a structured 2D matrix
		 */
		bool split_mdouble_hcST(int sindex, double *p1, double *p2);

		/*
		Prints out the mdouble array read, please call this after readcsv
		*/
		void show_mdouble();

		/*
		Free the main double array mdouble
		*/
		void freeall();

		/*
		Get the size of the rows read by the reader
		*/
		size_t getRowCount(){return mrowcount;};

		/*
		Get the size of the cols read by the reader
		*/
		size_t getColCount(){return mcolcount;};

		/*
		Destructor that goes is called when reader goes out of scope
		*/
		~DoubleReader(){freeall();}; //destructor

	};


}


#endif
