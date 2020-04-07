#!/usr/bin/python3

import sys
from Equation import Equation

argc = len(sys.argv)

if argc < 2:
    sys.exit("Missing argument")
elif argc > 2:
    sys.exit("Too much arguments")

e = Equation(sys.argv[1])
print("Input   form: ", e.format())
e.simplify()
print("Reduced form: ", e.format())
print("Polynomial degree: ",  e.degree())
if e.degree() > 2:
    print("The polynomial degree is stricly greater than 2, I can't solve.")
print("The solution is:")
print(e.solve())
