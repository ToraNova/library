#!/bin/bash

# compiles ctest with GCC instead of G++ to test the library
# using gcc to compile our library must include the -lstdc++ linker line behind
# because the library is inherently C++.
gcc test/cdrive.c test/csv_test.c test/support_test.c -o bin/gcc.test -Iinclude lib/libprodtools.a -lm -lstdc++ 

# also tests the shared library use
# you will need to set the LD_LIBRARY_PATH to include the lib directory in order to allow runtime loading
gcc test/cdrive.c test/csv_test.c test/support_test.c -o bin/gcc.shared.test -Iinclude -Llib -lprodtools_shared -lm -lstdc++
