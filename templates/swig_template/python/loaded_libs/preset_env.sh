
# setups the environment variable for runtime loading of shared libraries
# use . present_env.sh to source it
# project pyplasma - ToraNova 2019
export LD_LIBRARY_PATH=/home/cjason/library/prodtools/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/intel/mkl/lib/intel64
echo LD_LIBRARY_PATH current environment :
echo $LD_LIBRARY_PATH
