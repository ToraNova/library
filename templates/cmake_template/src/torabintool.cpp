/*
	cmake_boostrap
	Main binary source

	ToraNova
*/
//#include "torabintool.h"
#include <torabinutil.h>
#include <iostream>

static const char *const HEADER = "torabintools 2019 - CMAKE BOOTSTRAP\n\n";
static const char *const USAGE = "Usage : <input>\n";

int main(int argc, const char *argv[]) {

  std::cout << HEADER;

  // ensure the correct number of parameters are used.
  if (argc < 2) {
    std::cout << USAGE;
    return 1;
  }

  binlibtest();
  hexlibtest();
  ctestfunc();
  std::cout << argv[1] << std::endl;
  return 0;
}
