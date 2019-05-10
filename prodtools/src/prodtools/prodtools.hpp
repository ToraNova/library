/*

  Prodtools main header file
  FOR C/CXX USE
  this file consist of all the important headers
  for the prodtools project

  include this file to use all of prodtools functions

  @author ToraNova
  chia_jason96@live.com
*/

#ifndef PRODTOOLS_HPP
#define PRODTOOLS_HPP

#define TRUE 1
#define FALSE 0

//CXX headers (C/C++ projects should include this file for a "all include")

//SUPPORT modules
#include <prodtools/support/suprint.hpp>
#include <prodtools/support/convert.hpp>
#include <prodtools/support/turegex.hpp>

//NETWORK modules
#include <prodtools/network/tcpsock.hpp>

//ARRAYUTIL modules
#include <prodtools/arrayutil/all.hpp>
//#include <prodtools/arrayutil/doubles.hpp> //minimal include

//MATH modules
#include <prodtools/math/linear.hpp>

//CSV modules
#include <prodtools/csv/reader.hpp>
#include <prodtools/csv/writer.hpp>


#endif
