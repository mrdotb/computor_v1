#!/usr/bin/python3

import unittest
import Math
import Parser

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

class TestParser(unittest.TestCase):

    def test_parser_test1(self):
        equation = "5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0"
        expected = (
            [{'coeff': 5.0, 'indeterminate': 'X', 'degree': 0},
             {'coeff': -6.0, 'indeterminate': 'X', 'degree': 1},
             {'coeff': 0.0, 'indeterminate': 'X', 'degree': 2},
             {'coeff': -5.6, 'indeterminate': 'X', 'degree': 3}],
            []
        )
        self.assertEqual(Parser.parse(equation), expected)

    def test_parser_test2(self):
        equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" 
        expected = (
            [{'coeff': 5.0, 'indeterminate': 'X', 'degree': 0},
             {'coeff': 4.0, 'indeterminate': 'X', 'degree': 1},
             {'coeff': -9.3, 'indeterminate': 'X', 'degree': 2}],
            [{'coeff': 1.0, 'indeterminate': 'X', 'degree': 0}]
        )
        self.assertEqual(Parser.parse(equation), expected)




# tuple = Parser.parse("5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0")
# tuple = Parser.parse("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
# print(tuple)
unittest.main()
