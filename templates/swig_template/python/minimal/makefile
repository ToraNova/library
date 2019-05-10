# Makefile to build the wrapping objects

# project name
PRONAME  := pyplasma

.phony: all
all:
	python3 src/setup.py build_ext --inplace

.phony: clean
clean:
	rm -rf build
	rm -rf __pycache__
	rm -f ./*.o ./*.so ./*.pyc 
	rm -f ./*.c ./*.cxx ./$(PRONAME).py
