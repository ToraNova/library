#!/bin/bash

# clears all the builds from the install directory

rm -rf build
rm bin/* include/* lib/* -rf
touch bin/.gitkeep include/.gitkeep lib/.gitkeep
