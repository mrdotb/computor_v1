import re
# Term
# -5 * x ^ 2
# coeff is -5
# indeterminate is x
# degree is 2

pattern = re.compile("(-? ?\d\.?\d?) \* (X)\^(\d)")

def parse(str):
    split = str.split('=')
    left = split[0]
    right = split[1]
    return (group(left), group(right))

def group(str):
    list = []
    for (coeff, indeterminate, degree) in re.findall(pattern, str):
        coeff = float(coeff.replace(" ", ""))
        degree = int(degree)
        list.append(create_term(coeff, indeterminate, degree))
    return list

def create_term(coeff, indeterminate, degree):
    return {'coeff': coeff, 'indeterminate': indeterminate, 'degree': degree }
