import re
import copy

class Equation:
    """ Solve polynomial until degree 2 """
    state = ()
    # Term = coeff * indeterminate ^ degree
    pattern = re.compile("(-? ?\d+\.?\d*) \* (X)\^(\d+)")

    def __init__(self, equation_str):
        [left, right] = equation_str.split('=')
        self.state = (self.transform(left), self.transform(right))

    def get_state(self):
        return self.state

    def simplify(self):
        left = self.simplify_terms(self.state[0])
        right = self.simplify_terms(self.state[1])
        for a_index, a in enumerate(right):
            match = False
            for b_index, b in enumerate(left):
                if a['degree'] == b['degree']:
                    b['coeff'] -= a['coeff']
                    match = True
            if match == False:
                a['coeff'] *= -1
                left.append(a)

        self.state = (self.simplify_terms(left), [])

    def simplify_terms(self, terms):
        result = []
        degrees = []
        for a_index, a in enumerate(terms):
            term = copy.deepcopy(a)
            for b_index, b in enumerate(terms):
                if a_index == b_index or a['degree'] in degrees:
                    continue
                if a['degree'] == b['degree'] and a['inde'] == b['inde']:
                    term['coeff'] += b['coeff']
            if a['degree'] not in degrees:
                degrees.append(term['degree'])
                if term['coeff'] != 0:
                    result.append(term)

        return result

    def transform(self, equation_str_part):
        part = []
        for (coeff, inde, degree) in re.findall(self.pattern, equation_str_part):
            coeff = float(coeff.replace(" ", ""))
            degree = int(degree)
            part.append(self.create_term(coeff, inde, degree))
        return part

    def create_term(self, coeff, inde, degree):
        return {'coeff': coeff, 'inde': inde, 'degree': degree}

    def degree(self):
        terms = self.state[0] + self.state[1]
        max_degree = 0
        for term in terms:
            if term['degree'] > max_degree:
                max_degree = term['degree']
        return max_degree

    def solve(self):
        degree = self.degree()
        if degree == 0:
            return self.solve_degree0()
        elif degree == 1:
            return self.solve_degree1()
        elif degree == 2:
            return self.solve_degree2()

    def solve_degree0(self):
        (left, right) = self.state
        if len(left) == 0 and len(right) == 0:
            return 'True for all X.'
        if len(left) > 0 and len(right) == 0:
            return 'No solutions.'

    def solve_degree1(self):
        0

    def solve_degree2(self):
        0

    def format_coeff(self, nb, index):
        if index > 0 and nb < 0:
            nb *= -1
        if nb.is_integer():
            return str(int(nb))
        else:
            return str(nb)

    def format_side(self, part):
        string = ''
        for index, term in enumerate(part):
            if index != 0 and index < len(part):
                if term['coeff'] < 0:
                    string += ' - '
                else:
                    string += ' + '
            coeff = self.format_coeff(term['coeff'], index)
            string += '{coeff} * {term[inde]}^{term[degree]}'\
            .format(coeff=coeff, term=term)
        return string

    def format(self):
        string = ''
        (left, right) = self.state
        if len(left) == 0:
            string += '0'
        else:
            string += self.format_side(left)
        if len(right) == 0:
            string += ' = 0'
        else:
            string += ' = '
            string += self.format_side(right)
        return string

    def __repr__(self):
        return self.format()

    def __str__(self):
        return self.format()
