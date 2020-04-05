class Math():

    def pow(nb, power):
        if power == 0:
            return 1
        else:
            return nb * pow(nb, power - 1)

    def abs(nb):
        if nb > 0:
            return nb * -1
        else:
            return nb

    def sqrt(nb):
        return 1
