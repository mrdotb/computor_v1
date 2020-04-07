#!/usr/bin/python3

import unittest
import Math
import Parser
import Solver
from Equation import Equation

class TestMath(unittest.TestCase):

    def test_pow(self):
        self.assertEqual(Math.pow(10, 5), 10 ** 5)
        self.assertEqual(Math.pow(10, 4), 10 ** 4)
        self.assertEqual(Math.pow(10, 0), 10 ** 0)
        self.assertEqual(Math.pow(-10, 3), -10 ** 3)

    def test_abs(self):
        self.assertEqual(Math.abs(0), abs(0))
        self.assertEqual(Math.abs(-1), abs(-1))
        self.assertEqual(Math.abs(2), abs(2))

    def test_sqrt(self):
        self.assertEqual(Math.sqrt(0), 0)
        self.assertEqual(Math.sqrt(4), 2)
        self.assertEqual(Math.sqrt(7), 2.6457513110645907)
        self.assertEqual(Math.sqrt(125348), 354.04519485512014)
        self.assertEqual(Math.sqrt(133333333387), 365148.37174359686)

class TestEquation(unittest.TestCase):

    def test_parser_1(self):
        equation = "5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0"
        a = Equation(equation)
        expected = (
            [{'coeff': 5.0, 'inde': 'X', 'degree': 0},
             {'coeff': -6.0, 'inde': 'X', 'degree': 1},
             {'coeff': 0.0, 'inde': 'X', 'degree': 2},
             {'coeff': -5.6, 'inde': 'X', 'degree': 3}],
            []
        )
        self.assertEqual(a.get_state(), expected)

    def test_parser_2(self):
        equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" 
        a = Equation(equation)
        expected = (
            [{'coeff': 5.0, 'inde': 'X', 'degree': 0},
             {'coeff': 4.0, 'inde': 'X', 'degree': 1},
             {'coeff': -9.3, 'inde': 'X', 'degree': 2}],
            [{'coeff': 1.0, 'inde': 'X', 'degree': 0}]
        )
        self.assertEqual(a.get_state(), expected)

    def test_parser_3(self):
        equation = "5 * X^0 - 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" 
        a = Equation(equation)
        expected = (
            [{'coeff': 5.0, 'inde': 'X', 'degree': 0},
             {'coeff': -5.0, 'inde': 'X', 'degree': 0},
             {'coeff': 4.0, 'inde': 'X', 'degree': 1},
             {'coeff': -9.3, 'inde': 'X', 'degree': 2}],
            [{'coeff': 1.0, 'inde': 'X', 'degree': 0}]
        )
        self.assertEqual(a.get_state(), expected)

    def test_format_1(self):
        equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" 
        a = Equation(equation)
        self.assertEqual(a.format(), equation)

    def test_format_2(self):
        equation = "-5 * X^0 + 4 * X^1 - 9.3 * X^2 = -1 * X^0" 
        a = Equation(equation)
        self.assertEqual(a.format(), equation)

    def test_format_3(self):
        equation = "-5 * X^2 - 4 * X^0 - 9.3 * X^1 = -1 * X^0" 
        a = Equation(equation)
        self.assertEqual(a.format(), equation)

    def test_degree_1(self):
        equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" 
        a = Equation(equation)
        self.assertEqual(a.degree(), 2)

    def test_degree_2(self):
        equation = "1 * X^3 = 0" 
        a = Equation(equation)
        self.assertEqual(a.degree(), 3)

    def test_simplify_1(self):
        a = Equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
        simple = "4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0"
        a.simplify()
        self.assertEqual(a.format(), simple)

    def test_simplify_2(self):
        a = Equation("5 * X^0 - 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 0")
        simple = "4 * X^1 - 9.3 * X^2 = 0"
        a.simplify()
        self.assertEqual(a.format(), simple)

    def test_simplify_3(self):
        a = Equation("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
        simple = "5 * X^0 - 6 * X^1 - 5.6 * X^3 = 0"
        a.simplify()
        self.assertEqual(a.format(), simple)

    def test_simplify_4(self):
        a = Equation("42 * X^0 = 42 * X^0")
        simple = "0 = 0"
        a.simplify()
        self.assertEqual(a.format(), simple)

    def test_simplify_5(self):
        a = Equation("42 * X^0 + 42 * X^0 = 42 * X^0")
        simple = "42 * X^0 = 0"
        a.simplify()
        self.assertEqual(a.format(), simple)

    def test_simplify_5(self):
        a = Equation("42 * X^0 + 42 * X^0 - 42 * X^0= 42 * X^0")
        simple = "0 = 0"
        a.simplify()
        self.assertEqual(a.format(), simple)

    def test_solve_1(self):
        a = Equation("42 * X^0 = 42 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "True for all X.")

    def test_solve_2(self):
        a = Equation("43 * X^0 = 42 * X^0")
        a.simplify()
        # self.assertEqual(a.solve(), "True for all X")




    # def test_resolve_polynomial_degree0_1(self):
    #     a = Equation("42 * X^0 = 42 * X^0")
    #     a.simplify()
    #     a.resolve()
    #     # self.assertEqual(a.format(), simple)


# run_test_0_all_sol "42 * X^0 = 42 * X^0"
# run_test_0_no_sol  "0 * X^453 = 5"
# run_test_0_all_sol "0 * X^453 = 0"
# run_test_0_all_sol "5 * X^0 = 5 * X^0"
# run_test_0_all_sol "5 * X^0 + X^2 = 5 * X^0 + X^2"
# run_test_0_no_sol "5 * X^0 + X^2 = 5 * X^0 + X^2 + 1"
# run_test_0_no_sol "4 * X^0 = 8 * X^0"



# a = Equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
# a.simplify()
# print(a.format())

#print("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
unittest.main()

