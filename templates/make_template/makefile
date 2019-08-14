# ***********************************************
#                    ToraProjects
# ***********************************************

# DIR-STRUCTURE DECLARES
SRCDIR   = src
OBJDIR   = obj
BINDIR   = bin
TESTDIR   = test
SAMPLEDIR = sample
MAINDIR = main
IDIR = include

# generate the list of objects to be compiled
SOURCES  := $(wildcard $(SRCDIR)/*.c)
CPPSOURCES := $(wildcard $(SRCDIR)/*.cpp)
OBJECTS  := $(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.co)
OBJECTCPPS  := $(CPPSOURCES:$(SRCDIR)/%.cpp=$(OBJDIR)/%.cxx.o)

# generate the list of tests binaries
TESTS := $(wildcard $(TESTDIR)/*.c)
TESTP := $(TESTS:$(TESTDIR)/%.c=$(BINDIR)/%.testbin)
TESTCPPS := $(wildcard $(TESTDIR)/*.cpp)
TESTCPPP := $(TESTCPPS:$(TESTDIR)/%.cpp=$(BINDIR)/%.testbin)

# generate the list of sample binaries
SAMPLES := $(wildcard $(SAMPLEDIR)/*.c)
SAMPLEP := $(SAMPLES:$(SAMPLEDIR)/%.c=$(BINDIR)/%.sample)
SAMPLECPPS := $(wildcard $(SAMPLEDIR)/*.cpp)
SAMPLECPPP := $(SAMPLECPPS:$(SAMPLEDIR)/%.cpp=$(BINDIR)/%.sample)

# generate the list of target
MAINS := $(wildcard $(MAINDIR)/*.c)
MAINP := $(MAINS:$(MAINDIR)/%.c=$(BINDIR)/%.out)
MAINCPPS := $(wildcard $(MAINDIR)/*.cpp)
MAINCPPP := $(MAINCPPS:$(MAINDIR)/%.cpp=$(BINDIR)/%.out)

OBJECTFULL = $(OBJDIR)/*.co
CXXOBJS = $(OBJDIR)/*.cxx.o

# flags and compiler defines
CPP = g++
CC = gcc

CLIBS = -lm -lpthread -lrt -maes -msse4 -lmsgpackc -lcrypto -lgnutlsxx -lgnutls -lssl
CPPLIBS = -lm

CFLAGS= -O3 -Wall -march=native -I$(IDIR)
CPPFLAGS = -Wall -I$(IDIR)

# standard command defines
rm = rm --f
ls = ls

# default target
.PHONY: all
all:	tests samples mains
	@echo 'make done'
	@$(ls) $(BINDIR)

# mains - programs that are intended deliverables of the c/c++ project
.PHONY: mains
mains : $(MAINP) $(MAINCPPP)
	@echo 'Mains compiled'

$(MAINP) : $(BINDIR)/%.out: $(MAINDIR)/%.c $(OBJECTS) $(OBJECTCPPS)
	$(CC) $(OBJECTFULL) $< -o $@ $(CLIBS) $(CFLAGS)

$(MAINCPPP) : $(BINDIR)/%.out: $(MAINDIR)/%.cpp $(OBJECTS) $(OBJECTCPPS)
	$(CPP) $(SOURCES) $(CXXOBJS) $< -o $@ $(CPPLIBS) $(CPPFLAGS)

# samples - sample program to help implementation (usually for libs)
.PHONY: samples
samples : $(SAMPLEP) $(SAMPLECPPP)
	@echo 'Samples compiled'

$(SAMPLEP) : $(BINDIR)/%.sample : $(SAMPLEDIR)/%.c $(OBJECTS) $(OBJECTCPPS)
	$(CC) $(OBJECTFULL) $< -o $@ $(CLIBS) $(CFLAGS)

$(SAMPLECPPP) : $(BINDIR)/%.sample : $(SAMPLEDIR)/%.cpp $(OBJECTS) $(OBJECTCPPS)
	$(CPP) $(SOURCES) $(CXXOBJS) $< -o $@ $(CPPLIBS) $(CPPFLAGS)

# tests - unit tests made to ensure the functionality and correctness of the library
.PHONY: tests
tests :	$(TESTP) $(TESTCPPP)
	@echo 'Tests Compiled'

$(TESTP) : $(BINDIR)/%.testbin : $(TESTDIR)/%.c $(OBJECTS) $(OBJECTCPPS)
	$(CC) $(OBJECTFULL) $< -o $@ $(CLIBS) $(CFLAGS)

$(TESTCPPP) : $(BINDIR)/%.testbin : $(TESTDIR)/%.cpp $(OBJECTS) $(OBJECTCPPS)
	$(CPP) $(SOURCES) $(CXXOBJS) $< -o $@ $(CPPLIBS) $(CPPFLAGS)

# objects
$(OBJECTS) : $(OBJDIR)/%.co : $(SRCDIR)/%.c
	$(CC) -c $< -o $@ $(CLIBS) $(CFLAGS)

$(OBJECTCPPS) : $(OBJDIR)/%.cxx.o : $(SRCDIR)/%.cpp
	$(CPP) -c $< -o $@ $(CPPLIBS) $(CPPFLAGS)

# utils - cleanup
.PHONEY: clean
clean:
	@echo "Clearing builds..."
	@$(rm) $(OBJDIR)/*
	@$(rm) $(BINDIR)/*

# debugging
.PHONEY: print_targets
print_targets:
	@echo $(OBJECTS)
	@echo $(OBJECTCPPS)
	@echo $(TESTP)
	@echo $(TESTCPPP)
	@echo $(SAMPLEP)
	@echo $(SAMPLECPPP)
	@echo $(MAINP)
	@echo $(MAINCPPP)


