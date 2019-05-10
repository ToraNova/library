/*
  Project Prodtools
  Prodtools is a library for the sake of c/c++ development speed

  Modular C wrapper file

  @author ToraNova
  @version 1.0 April 29,2019
  @mailto chia_jason96@live.com
*/

//original c++ implementation
#include "timing.hpp"
//wrapper header
#include "timing.h"
#include <time.h>

//wrapper for the function libtest
void timing_libtest(){
	timing::libtest();
}

timing_SimpleCPUTimer *constr_SimpleCPUTimer(){
	timing::SimpleCPUTimer *out = new timing::SimpleCPUTimer();
	return reinterpret_cast<timing_SimpleCPUTimer *>(out);
}

void SimpleCPUTimer_begin(timing_SimpleCPUTimer *cptr){
	timing::SimpleCPUTimer *ctx = reinterpret_cast<timing::SimpleCPUTimer *>(cptr);
	ctx->begin();
	return;
}

void SimpleCPUTimer_end(timing_SimpleCPUTimer *cptr){
	timing::SimpleCPUTimer *ctx = reinterpret_cast<timing::SimpleCPUTimer *>(cptr);
	ctx->end();
	return;
}

void SimpleCPUTimer_print(timing_SimpleCPUTimer *cptr){
	timing::SimpleCPUTimer *ctx = reinterpret_cast<timing::SimpleCPUTimer *>(cptr);
	ctx->print();
	return;
}

double SimpleCPUTimer_getdiff_secs(timing_SimpleCPUTimer *cptr){
	timing::SimpleCPUTimer *ctx = reinterpret_cast<timing::SimpleCPUTimer *>(cptr);
	return ctx->getdiff_secs();
}

clock_t SimpleCPUTimer_getdiff(timing_SimpleCPUTimer *cptr){
	timing::SimpleCPUTimer *ctx = reinterpret_cast<timing::SimpleCPUTimer *>(cptr);
	return ctx->getdiff();
}

void destr_SimpleCPUTimer( timing_SimpleCPUTimer *cptr){
	timing::SimpleCPUTimer *ctx = reinterpret_cast<timing::SimpleCPUTimer *>(cptr);
	delete ctx;
	return;
}

timing_SimpleWallTimer *constr_SimpleWallTimer(){
	timing::SimpleWallTimer *out = new timing::SimpleWallTimer();
	return reinterpret_cast<timing_SimpleWallTimer *>(out);
}

void SimpleWallTimer_begin(timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	ctx->begin();
	return;
}

void SimpleWallTimer_end(timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	ctx->end();
	return;
}

void SimpleWallTimer_print(timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	ctx->print();
	return;
}

double SimpleWallTimer_getstart_secs(timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	return ctx->getstart_secs();
}

double SimpleWallTimer_getstop_secs(timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	return ctx->getstop_secs();
}

double SimpleWallTimer_getdiff_secs(timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	return ctx->getdiff_secs();
}

void destr_SimpleWallTimer( timing_SimpleWallTimer *cptr){
	timing::SimpleWallTimer *ctx = reinterpret_cast<timing::SimpleWallTimer *>(cptr);
	delete ctx;
	return;
}


