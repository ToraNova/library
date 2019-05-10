/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular header file
  April 22 2019

  @author ToraNova
  @version 1.2 April 22,2019
  @mailto chia_jason96@live.com
*/

#ifndef READER_H
#define READER_H

#include <stdint.h>
#include <string.h>

typedef struct csvreader_DoubleReader csvreader_DoubleReader;

#ifdef __cplusplus
extern "C" {
#endif

void csvreader_libtest();

/*
  C wrapped object oriented code
*/
csvreader_DoubleReader *constr_DoubleReader();
int DoubleReader_readcsv(csvreader_DoubleReader *cptr, const char *filename, int skipfirst);
double **DoubleReader_borrow_mdouble(csvreader_DoubleReader *cptr);

int DoubleReader_split_mdouble_vc(csvreader_DoubleReader *cptr,int sindex, double **spA, double **spB);
int DoubleReader_split_mdouble_vcST(csvreader_DoubleReader *cptr,int sindex, double *spA, double *spB);
int DoubleReader_split_mdouble_hc(csvreader_DoubleReader *cptr,int sindex, double **spA, double **spB);
int DoubleReader_split_mdouble_hcST(csvreader_DoubleReader *cptr,int sindex, double *spA, double *spB);

void DoubleReader_show_mdouble(csvreader_DoubleReader *cptr);
void DoubleReader_freeall(csvreader_DoubleReader *cptr);
size_t DoubleReader_getRowCount(csvreader_DoubleReader *cptr);
size_t DoubleReader_getColCount(csvreader_DoubleReader *cptr);
void destr_DoubleReader(csvreader_DoubleReader *cptr);


#ifdef __cplusplus
};
#endif

#endif
