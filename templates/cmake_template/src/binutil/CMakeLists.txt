# requires a cmake version
cmake_minimum_required(VERSION 3.1)

# TODO: Please edit the root cmakelist file to include the new module
# name after setup lib name. This allows other sources to link
# indicate that the library is in c/c++
set(module_name "torabinutil")
project(${module_name} C CXX)

# TODO: specify sources here
set(sources
    binary.cpp
    hex.cpp
    ctest.c
)

set(headers
    torabinutil.h
)

add_library(${module_name} SHARED STATIC ${sources} ${headers})
# move these files onto their install locations
install(TARGETS ${module_name} DESTINATION ${cproject_install_lib_dir})
install(FILES ${headers} DESTINATION ${cproject_install_include_dir})
