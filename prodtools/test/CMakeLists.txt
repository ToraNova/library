# requires a cmake version
cmake_minimum_required(VERSION 3.14.1)

project(tests C CXX)

# TODO: Add test units here
# source file listing
set(tsources
	xdrive.cpp
	support_test.cpp
	csv_test.cpp
	network_test.cpp
)

set(csources
	cdrive.c
	support_test.c
	csv_test.c
)

# TODO: Add compiling targets here
# specify "drive" to be compiled from sources
add_executable(xdrive ${tsources})
add_executable(cdrive ${csources})

# link the libraries
target_link_libraries(xdrive ${compiled_libraries} ${extern_libraries})
target_link_libraries(cdrive ${compiled_libraries} ${extern_libraries})

# install "drive" to "bin"
# this will copy the "drive" executable
# onto the bin directory on the template
# project
install(TARGETS xdrive cdrive DESTINATION ${cproject_install_bin_dir})
