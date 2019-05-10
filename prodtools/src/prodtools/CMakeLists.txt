# requires a cmake version
cmake_minimum_required(VERSION 3.14.1)

# Dev-notebook TODO LIST
# WIP : merge this 4 with a for loop
# WIP : merge all the four following into one todo specify

# TODO: add new directories for library submodules here
# The directory name should be the same as the module name
add_subdirectory(support)
add_subdirectory(csv)
add_subdirectory(arrayutil)
add_subdirectory(network)
add_subdirectory(math)

# TODO: list the includes
include_directories(support)
include_directories(csv)
include_directories(arrayutil)
include_directories(network)
include_directories(math)

# TODO: include the modules for the library
set(libmodules
	$<TARGET_OBJECTS:support_module>
	$<TARGET_OBJECTS:csv_module>
	$<TARGET_OBJECTS:arrayutil_module>
	$<TARGET_OBJECTS:network_module>
	$<TARGET_OBJECTS:math_module>
)

# TODO: specify the shared modules as well
set(libmodules_shared
	$<TARGET_OBJECTS:support_module_shared>
	$<TARGET_OBJECTS:csv_module_shared>
	$<TARGET_OBJECTS:arrayutil_module_shared>
	$<TARGET_OBJECTS:network_module_shared>
	$<TARGET_OBJECTS:math_module_shared>
)

#--------------------------------------------------------------
# builds the static library libprodtools.a
#--------------------------------------------------------------
add_library(prodtools
	STATIC
	${libmodules}
)
#--------------------------------------------------------------

#--------------------------------------------------------------
# builds the shared object libprodtools.so
#--------------------------------------------------------------
add_library(prodtools_shared
	SHARED
	${libmodules_shared}
)
#--------------------------------------------------------------

#--------------------------------------------------------------
# main headers
#--------------------------------------------------------------
set(main_header
	ptdebug.h
	ptmodheaders.hpp
	prodtools.hpp
	prodtools.h
)
#--------------------------------------------------------------

#--------------------------------------------------------------
# Persistence
# installation rules
#--------------------------------------------------------------
install(TARGETS prodtools prodtools_shared DESTINATION ${cproject_install_lib_dir}) # installs the library
install(FILES ${main_header} DESTINATION ${cproject_install_include_dir}/${project_name}) # installs the headers
#--------------------------------------------------------------
