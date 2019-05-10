#
#   MAIN CMAKE FILE - prodtools
#   ToraNova 2019
#
# Specify a required minimum version
cmake_minimum_required(VERSION 3.14.1)

# Project name setup
set(project_name "prodtools")
project(${project_name} C CXX)

# declare cmake cpp flags
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

# CMAKE_INSTALL_PREFIX can be changed to /usr/local or /usr to allow
# system wide installation
set(cproject_install_prefix ${PROJECT_SOURCE_DIR})
set(cproject_install_include_dir ${cproject_install_prefix}/include/${projct_name} )
set(cproject_install_bin_dir ${cproject_install_prefix}/bin)
set(cproject_install_lib_dir ${cproject_install_prefix}/lib)

include_directories(${cproject_install_include_dir})
include_directories(src)

# LIBRARY DECLARAIONS
# TODO: please add any compiled library targets here
set(compiled_libraries prodtools)

add_subdirectory(src/prodtools)
add_subdirectory(test)
