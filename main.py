#!/usr/bin/python3

import sys
import Math

argc = len(sys.argv)

if argc < 2:
    sys.exit("Missing argument")
elif argc > 2:
    sys.exit("Too much arguments")

equation = sys.argv[1]
print(equation)
