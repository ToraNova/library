# requires a cmake version
cmake_minimum_required(VERSION 3.14.1)

#--------------------------------------------------------------
# The directory name is the module name
# by convention, the module name is prepended
# with the directory name <dir>_module for
# prodtools modules -as of version 1.0 - ToraNova
#--------------------------------------------------------------

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -msse4 -maes")

#--------------------------------------------------------------
# TODO section : Please go through this section
# and perform the todos requested
#--------------------------------------------------------------
# TODO: change the module name
set(module_name math)

# TODO: declare the source files
set(module_sources
  linear.cpp
  linear_cwrap.cpp
)

# TODO: specify linked libraries (local or external)
#set(module_dependence
#	arrayutil_module
#)

# TODO: declares the header files
# use hpp for cpp headers while
# h for c headers
set("${module_name}_headers"
  linear.hpp
  linear.h
)

#--------------------------------------------------------------
# Persistence; target setup
# compile objects for the static library
# and link the static library file with its
# dependencies
#--------------------------------------------------------------
add_library(
	"${module_name}_module"
	OBJECT
	${module_sources}
)

# link
target_link_libraries( "${module_name}_module"
  ${module_dependence}
)

#--------------------------------------------------------------
# Persistence; target setup
# compile objects for the shared library
# and link the shared library file with
# its dependencies
#--------------------------------------------------------------
add_library(
	"${module_name}_module_shared"
	OBJECT
	${module_sources}
)
# set property for position independent code (shared obj requirement)
set_property(TARGET "${module_name}_module_shared" PROPERTY POSITION_INDEPENDENT_CODE ON)
	
# link
target_link_libraries( "${module_name}_module_shared"
  ${module_dependence}
)

#--------------------------------------------------------------
# Persistence; setups the installation
# installation rules
#--------------------------------------------------------------
install(FILES ${${module_name}_headers}
        DESTINATION ${cproject_install_include_dir}/${project_name}/${module_name}
        )
