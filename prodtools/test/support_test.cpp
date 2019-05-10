/*
  Project Prodtools
  Test driver module

  module for support testing

  ToraNova 2019
  chia_jason96@live.com
*/
#include "testlist.hpp"

#include <prodtools/support/suprint.hpp>
#include <prodtools/arrayutil/all.hpp>
using namespace std;

void support_test0(){
	suprint::libtest();

	double t1[9] = {1,1,1,2,2,2,3,3,3};

	double **t2 = arrayutil::doubles::array12split( t1, 3, 3);

	suprint::doublearr2D( t2, 3, 3);


	return;
}
