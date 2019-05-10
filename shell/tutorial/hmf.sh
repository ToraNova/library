#!/bin/bash
#f which is the number of file
#is evaluated literally by running the expression in bash
f='ls -l | wc -l'
#the expression returns the number of file +1
#ls pipes -l returns the number of files, each file being a newline
#wc is a wordcount function, it returns the number of newlines (for -l)
#when fed in a file.
