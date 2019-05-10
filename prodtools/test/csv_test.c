/*
  Project Prodtools
  Test driver module

  module for csv testing

  ToraNova 2019
  chia_jason96@live.com
*/
#include "testlist.h"

#include <prodtools/csv/writer.h>
#include <prodtools/csv/reader.h>
#include <prodtools/support/suprint.h> //lol, suprint is used here as well
#include <prodtools/arrayutil/all.h> //lol this as well

#define TEST_ST
void csv_test0(){
	csvwriter_libtest();

	csvreader_DoubleReader *rd = constr_DoubleReader();
	int res = DoubleReader_readcsv(rd,"assets/double.csv",0);
	printf("Read results %d\n",res);

	size_t i;//counter
	DoubleReader_show_mdouble(rd);
	//memory alloc for test arrays
#ifndef TEST_ST
	printf("Performing Non_ST Test\n");
	double **vsplitA = arrayutil_doubles_allocdim( DoubleReader_getRowCount(rd), 3);
	double **vsplitB = arrayutil_doubles_allocdim( DoubleReader_getRowCount(rd), 5);
	double **hsplitA = arrayutil_doubles_allocdim( 50, DoubleReader_getColCount(rd));
	double **hsplitB = arrayutil_doubles_allocdim( 50, DoubleReader_getColCount(rd));

	printf("Memory allocation OK\n");
	DoubleReader_split_mdouble_vc(rd, 3 , vsplitA, vsplitB);
	printf("split vc OK\n");
	DoubleReader_split_mdouble_hc(rd, 50, hsplitA, hsplitB);
	printf("split hc OK\n");

	suprint_doublearr2D(vsplitA, DoubleReader_getRowCount(rd), 3, 10, 3);
	suprint_doublearr2D(vsplitB, DoubleReader_getRowCount(rd), 5, 10, 3);
	suprint_doublearr2D(hsplitB, 50, DoubleReader_getColCount(rd), 10, 3);
	suprint_doublearr2D(hsplitA, 50, DoubleReader_getColCount(rd), 10, 3);

	arrayutil_doubles_freedim(vsplitA, DoubleReader_getRowCount(rd));	
	arrayutil_doubles_freedim(vsplitB, DoubleReader_getRowCount(rd));	
	arrayutil_doubles_freedim(hsplitA, 50);	
	arrayutil_doubles_freedim(hsplitB, 50);	
#else
	printf("Performing ST Test");
	double *vsplitAST = (double *)malloc(sizeof(double) * DoubleReader_getRowCount(rd) * 3);
	double *vsplitBST = (double *)malloc(sizeof(double) * DoubleReader_getRowCount(rd) * 5);
	double *hmicroAST = (double *)malloc(sizeof(double) * 40 * 5);
	double *hmicroBST = (double *)malloc(sizeof(double) * 60 * 5);
	double *hsplitAST = (double *)malloc(sizeof(double) * DoubleReader_getColCount(rd) * 50);
	double *hsplitBST = (double *)malloc(sizeof(double) * DoubleReader_getColCount(rd) * 50);
	double *vmicroAST = (double *)malloc(sizeof(double) * 50 * 6);
	double *vmicroBST = (double *)malloc(sizeof(double) * 50 * 2);
	printf("Memory allocation OK\n");
	DoubleReader_split_mdouble_vcST(rd, 3, vsplitAST, vsplitBST);
	arrayutil_doubles_split_hcSST( 40, vsplitBST, 100, 5, hmicroAST, hmicroBST); 
	printf("split vcST OK\n");
	DoubleReader_split_mdouble_hcST(rd, 50, hsplitAST, hsplitBST);
	arrayutil_doubles_split_vcSST( 6, hsplitAST, 50, 8, vmicroAST, vmicroBST);
	printf("split hcST OK\n");

	/*
	suprint_doublearrST(vsplitAST, DoubleReader_getRowCount(rd), 3, 10, 3);
	suprint_doublearrST(vsplitBST, DoubleReader_getRowCount(rd), 5, 10, 3);
	suprint_doublearrST(hsplitBST, 50, DoubleReader_getColCount(rd), 10, 3);
	suprint_doublearrST(hsplitAST, 50, DoubleReader_getColCount(rd), 10, 3);
	*/

	suprint_doublearrST( vmicroAST, 50, 6, 10,3);
	suprint_doublearrST( vmicroBST, 50, 2, 10,3);

	free(vsplitAST);
	free(vsplitBST);
	free(hsplitAST);
	free(hsplitBST);
#endif

	csvwriter_writecsv_double(
	"assets/c_test_output.csv",
	DoubleReader_borrow_mdouble(rd),
	DoubleReader_getRowCount(rd),
	DoubleReader_getColCount(rd),
	';'
	);

	destr_DoubleReader(rd);

	return;

}
