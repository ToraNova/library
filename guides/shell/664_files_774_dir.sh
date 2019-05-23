#!/bin/bash

# perform a find, execute chmod 774 on directories and chmod 664 on files
dir="some sample directory"
find $dir \( -type d -exec chmod 774 {} \; \) -o \( -type f -exec chmod 664 {} \; \)
