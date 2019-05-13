# Make file for ToraNova's C programming library

TORALIBDIR=toralib
TESTDRVDIR=test_drv

# Generate list of sources
cdrv_sources=$(wildcard test_drv/*.c)
cdrv_headers=$(wildcard test_drv/*.h)
tests=$(cdrv_sources:.c=.testd) #generate a list of target test objs

clib_sources=$(wildcard toralib/*.c)
clib_headers=$(wildcard toralib/*.h)
clib_objs=$(clib_sources:.c=.o) #generate a list of target lib objs

GENLIB_NAME=toralib.so

# Makefile defines
CC=gcc
CFLAGS=-g -Wall

$(clib_objs): CFLAGS := -g -Wall -fPIC -lm
$(tests): CFLAGS := -g -Wall -I toralib toralib.so

#all is not an actual file, thus we use the phony keyword
.PHONY: all 
all: toralib.so ${tests}
	@echo 'building all...'

.PHONY: test
test: ${tests}
	@echo 'compiling tests...'	

#create main testd (test driver) files from main_drv
$(TESTDRVDIR)/%.testd : $(TESTDRVDIR)/%.c
	$(CC) -o $@ $< $(CFLAGS)

#create toralib so (require clib objs to be built first)
toralib.so: ${clib_objs}
	$(CC) -shared -fPIC -o $@ $^ -lc

#create obj files from toralib (position independent code PIC)
%.o : $(TORALIBDIR)/%.c
	$(CC) -o $@ $< $(CFLAGS)

.PHONY: clean
#clean the obj and the so file
clean :
	@echo 'Removing build files...'
	rm -f ${clib_objs} ${tests} $(GENLIB_NAME)

