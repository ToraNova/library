#!/bin/bash

# java apps
# quick script to compile and run for testing

if [ -z "$1" ]; then
	javac -cp "/usr/share/java/bcprov-ext-jdk13-164.jar:/usr/share/java/bcpkix-jdk13-164.jar" BC25519.java
	echo Compiled BC25519.java
	exit 0
fi

java -cp ".:/usr/share/java/bcprov-ext-jdk13-164.jar:/usr/share/java/bcpkix-jdk13-164.jar" BC25519 $1
exit 0

