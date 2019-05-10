#
#   MAIN CMAKE FILE - cmake_boostrap
#   ToraNova 2019
#
# Specify a required minimum version
cmake_minimum_required(VERSION 3.2)

# Project name setup
set(project_name "cmake_template")
project(${project_name} C CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O3")
set(extern_libraries "")

# CMAKE_INSTALL_PREFIX can be changed to /usr/local or /usr to allow
# system wide installation
set(cproject_install_prefix ${PROJECT_SOURCE_DIR})
set(cproject_install_include_dir ${cproject_install_prefix}/include)
set(cproject_install_bin_dir ${cproject_install_prefix}/bin)
set(cproject_install_lib_dir ${cproject_install_prefix}/lib)

include_directories(${cproject_install_include_dir})

# LIBRARY DECLARAIONS
# TODO: please add any compiled library targets here
set(compiled_libraries torabinutil)

# TODO : please edit this according to the libraries
set(BINTOOLS_HEADERS_DIR ${PROJECT_SOURCE_DIR}/src/binutil)

include_directories(${BINTOOLS_HEADERS_DIR})

add_subdirectory(src)
add_subdirectory(test)
