#!/usr/bin/env python3

import unittest
import my_math
from Equation import Equation

class TestMyMath(unittest.TestCase):

    def test_pow(self):
        self.assertEqual(my_math.pow(10, 5), 10 ** 5)
        self.assertEqual(my_math.pow(10, 4), 10 ** 4)
        self.assertEqual(my_math.pow(10, 0), 10 ** 0)
        self.assertEqual(my_math.pow(-10, 3), -10 ** 3)

    def test_abs(self):
        self.assertEqual(my_math.abs(0), abs(0))
        self.assertEqual(my_math.abs(-1), abs(-1))
        self.assertEqual(my_math.abs(2), abs(2))

    def test_sqrt(self):
        self.assertEqual(my_math.sqrt(0), 0)
        self.assertEqual(my_math.sqrt(4), 2)
        self.assertEqual(my_math.sqrt(7), 2.6457513110645907)
        self.assertEqual(my_math.sqrt(125348), 354.04519485512014)
        self.assertEqual(my_math.sqrt(133333333387), 365148.37174359686)

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
        self.assertEqual(a.solve(), "No solutions.")

    def test_solve_3(self):
        a = Equation("1 * X^0 + 1 * X^1 = 0 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = -1")

    def test_solve_4(self):
        a = Equation("1 * X^1 = 0 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = 0")

    def test_solve_5(self):
        a = Equation("3 * X^0 + 2 * X^1 = -45 * X^1 + 3 * X^0 + 9 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = 0.19148936170212766")

    def test_solve_6(self):
        a = Equation("-12.5 * X^1 - 3.4665 * X^0 = 0 * X^2 - 1 * X^1")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = -0.30143478260869566")

    def test_solve_7(self):
        a = Equation("5 * X^0 + 4 * X^1 = 4 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = -0.25")

    def test_solve_8(self):
        a = Equation("5 * X^0 + 4 * X^1 + 1 * X^2 = 1 * X^2")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = -1.25")

    def test_solve_9(self):
        a = Equation("5 * X^0 = 4 * X^0 + 7 * X^1")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = 0.14285714285714285")

    def test_solve_10(self):
        a = Equation("5 * X^0 = 4 * X^0 + 7 * X^1")
        a.simplify()
        self.assertEqual(a.solve(), "The solution is:\nX = 0.14285714285714285")

    def test_solve_11(self):
        a = Equation("1 * X^2 + 2 * X^1 + 1 * X^0 = 0 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is 0:\n-1")

    def test_solve_12(self):
        a = Equation("-2 * X^2 + 2 * X^1 + 1 * X^0 = -2 * X^2 + 1 * X^2 + 2 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is 0:\n1")

    def test_solve_13(self):
        a = Equation("6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is 0:\n-1")

    def test_solve_14(self):
        a = Equation("1 * X^2 + 34 * X^1 + 1 * X^0 = 0 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is strictly positive, the two solutions are:\n-0.029437251522857366\n-33.97056274847714")

    def test_solve_15(self):
        a = Equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is strictly positive, the two solutions are:\n-0.47513146390886934\n0.9052389907905898")

    def test_solve_16(self):
        a = Equation("5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is strictly positive, the two solutions are:\n-0.3670068381445481\n-3.632993161855452")

    def test_solve_17(self):
        a = Equation("1 * X^2 + 1 * X^1 + 1 * X^0 = 0 * X^0")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is strictly negative, the two complex solutions are:\n-0.5 + i * 0.8660254037844386\n-0.5 - i * 0.8660254037844386")

    def test_solve_18(self):
        a = Equation("3 * X^0 + 1 * X^1 = 0 * X^0 - 1 * X^1 - 3 * X^2")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is strictly negative, the two complex solutions are:\n-0.3333333333333333 + i * 0.9428090415820632\n-0.3333333333333333 - i * 0.9428090415820632")

    def test_solve_19(self):
        a = Equation("5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1")
        a.simplify()
        self.assertEqual(a.solve(), "Discriminant is strictly negative, the two complex solutions are:\n-0.5 + i * 1.0408329997330663\n-0.5 - i * 1.0408329997330663")

unittest.main()

