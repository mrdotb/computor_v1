def pow(nb, power):
    if power == 0:
        return 1
    else:
        return nb * pow(nb, power - 1)

def abs(nb):
    if nb < 0:
        return nb * -1
    else:
        return nb

def babylonian_method(nb):
    x = 10 * pow(10, 6) #precision
    prev = 1
    while prev != x:
        prev = x
        x = 1/2 * (prev + nb/prev)
    return prev

def sqrt(nb):
    if nb == 0:
        return 0
    else:
        return babylonian_method(nb)
