#!/usr/bin/env bash

# helps verify that some lesser-known words are indeed in the dictionary

while true; do
	read line
	egrep "^$line$" english.txt
done
