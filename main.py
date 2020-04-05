#!/usr/bin/python3

import sys

argc = len(sys.argv)

if argc < 2:
    sys.exit("Missing argument")
elif argc > 2:
    sys.exit("Too much arguments")

equation = sys.argv[1]
print(equation)

test =  babylonian_method(125348)
print(test)
