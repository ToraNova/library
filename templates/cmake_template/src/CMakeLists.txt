# requires a cmake version
cmake_minimum_required(VERSION 3.1)

# TODO: add new directories here
add_subdirectory("binutil")

# TODO: setup sources for the main program
set(msources "torabintool.cpp")

# TODO: setup the compile rules
set(exe_name "torabin")
# rule to compile ${exe_name} from sources
add_executable(${exe_name} ${msources})

# link torabin to torabintools
target_link_libraries(${exe_name} ${compiled_libraries} ${extern_libraries})

# installation rules
install(TARGETS ${exe_name} DESTINATION ${cproject_install_bin_dir})
