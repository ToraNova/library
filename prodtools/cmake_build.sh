#!/bin/bash

# cd into the build directory, clears it and runs cmake .. from it
# then we perform an install onto the project path (NOT system)
# then cd back onto the project root

mkdir -p build && cd build
cmake ..
make
make install
cd ..

