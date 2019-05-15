#!/bin/bash

# clears the build directory and 
# attempts a cmake_build

rm -rf build
rm bin/* include/* lib/*
touch bin/.gitkeep include/.gitkeep lib/.gitkeep
./cmake_build.sh
