#!/bin/bash

# java apps
# quick script to compile and run for testing

javac -cp "/usr/share/java/bcprov-ext-jdk13-164.jar" BC25519.java
java -cp ".:/usr/share/java/bcprov-ext-jdk13-164.jar" BC25519
