#!/usr/bin/env python3
# This tool is creating from emaildomain.com, to rules.
# Usage: ./domainConvert.py file.txt output.rule
import sys

with open(sys.argv[1], 'r') as passFile:
    passList = passFile.read().splitlines()

for line in passList:
    val = ""
    incr = 0
    for c in line.rstrip():
        if incr == 0 and c != "@":
            val = "$@"
        else:
            val += "$" + c
        incr += 1
    with open(sys.argv[2], "a") as myFile:
        myFile.write(val + "\n")
