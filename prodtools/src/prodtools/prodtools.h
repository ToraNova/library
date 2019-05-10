/*

  Prodtools main header file
  FOR C/CXX USE
  this file consist of all the important headers
  for the prodtools project

  include this file to use all of prodtools functions

  @author ToraNova
  chia_jason96@live.com
*/

#ifndef PRODTOOLS_H
#define PRODTOOLS_H

#define TRUE 1
#define FALSE 0

//Pure C headers
//Projects that are C based

//SUPPORT modules
#include <prodtools/support/suprint.h>

//CSV modules
#include <prodtools/csv/writer.h>
#include <prodtools/csv/reader.h>

//ARRAYUTIL modules
#include <prodtools/arrayutil/all.h>
//#include <prodtools/arrayutil/doubles.h> //minimal include

//NETWORK modules
#include <prodtools/network/simplesock.h>

//MATH modules
#include <prodtools/math/linear.h>

#endif
