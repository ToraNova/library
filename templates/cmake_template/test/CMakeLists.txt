# requires a cmake version
cmake_minimum_required(VERSION 3.1)


# TODO: Add test units here
# source file listing
set(tsources
	test_drive.cpp
)

# TODO: Add compiling targets here
# specify "drive" to be compiled from sources
add_executable(drive ${tsources})

# link the libraries
target_link_libraries(drive ${compiled_libraries} ${extern_libraries})

# install "drive" to "bin"
# this will copy the "drive" executable
# onto the bin directory on the template
# project
install(TARGETS drive DESTINATION ${PROJECT_SOURCE_DIR}/bin)
