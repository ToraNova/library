/**
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular C wrapper file
  April 22 2019

  @author ToraNova
  @version 1.2 April 22,2019
  @mailto chia_jason96@live.com
*/

#include "reader.h"
#include "reader.hpp"

/*
	CPP wrapper for a Object "DoubleReader"
*/

void csvreader_libtest(){
	csvreader::libtest();
}

csvreader_DoubleReader *constr_DoubleReader(){
	csvreader::DoubleReader *out = new csvreader::DoubleReader();
	return reinterpret_cast<csvreader_DoubleReader*>(out);
}

int DoubleReader_readcsv(csvreader_DoubleReader *cptr, const char *filename, int skipfirst){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return ctx->readcsv(filename,skipfirst);
}

double **DoubleReader_borrow_mdouble(csvreader_DoubleReader *cptr){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return ctx->borrow_mdouble();
}

void DoubleReader_show_mdouble(csvreader_DoubleReader *cptr){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	ctx->show_mdouble();
	return;
}

void DoubleReader_freeall(csvreader_DoubleReader *cptr){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	ctx->freeall();
	return;
}


size_t DoubleReader_getRowCount(csvreader_DoubleReader *cptr){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return (ctx->getRowCount());
}

size_t DoubleReader_getColCount(csvreader_DoubleReader *cptr){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return (ctx->getColCount());
}

void destr_DoubleReader(csvreader_DoubleReader *cptr){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	delete ctx;
	return;
}

int DoubleReader_split_mdouble_vc(csvreader_DoubleReader *cptr,int sindex, double **spA, double **spB){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return ctx->split_mdouble_vc(sindex,spA,spB);
}

int DoubleReader_split_mdouble_vcST(csvreader_DoubleReader *cptr,int sindex, double *spA, double *spB){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return ctx->split_mdouble_vcST(sindex,spA,spB);
}
int DoubleReader_split_mdouble_hc(csvreader_DoubleReader *cptr,int sindex, double **spA, double **spB){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return ctx->split_mdouble_hc(sindex,spA,spB);
}

int DoubleReader_split_mdouble_hcST(csvreader_DoubleReader *cptr,int sindex, double *spA, double *spB){
	csvreader::DoubleReader *ctx = reinterpret_cast<csvreader::DoubleReader *>(cptr);
	return ctx->split_mdouble_hcST(sindex,spA,spB);
}

