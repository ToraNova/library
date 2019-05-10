/*
	Project Prodtools
	Main test driver for all testing purposes

	ToraNova
*/


#include <prodtools/ptdebug.h>
#include <iostream>

#include "testlist.hpp"

int main(int argc, char *argv[]) {

	csv_test0();
	network_test0();
	support_test0();
	return 0;
}
