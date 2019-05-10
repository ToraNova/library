/*
  Project Prodtools
  Test driver module

  module for network testing

  ToraNova 2019
  chia_jason96@live.com
*/
#include "testlist.hpp"

#include <prodtools/network/tcpsock.hpp>
using namespace std;

void network_test0(){
  tcpsock::libtest();

  int s = sockgen(0);

  return;
}
