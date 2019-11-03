import unittest
from Calculator import Calculator
from CSVReader import read
from decimal import Decimal

class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        my_list=read('/src/Unit_Test_Addition.csv')
        for row in my_list:
         self.assertEqual(self.calculator.add(int(row[0]),int(row[1])), int(row[2]))

    def test_subtraction(self):
             my_list = read('/src/Unit_Test_Subtraction.csv')
             for row in my_list:
                 self.assertEqual(self.calculator.sub(int(row[0]), int(row[1])), int(row[2]))

    def test_multiplication(self):
        my_list = read('/src/Unit_Test_Multiplication.csv')
        for row in my_list:
            self.assertEqual(self.calculator.mul(int(row[0]), int(row[1])), int(row[2]))

    def test_division(self):
        my_list = read('/src/Unit_Test_Division.csv')
        for row in my_list:
            self.assertEqual(self.calculator.div(int(row[0]), int(row[1])), float(row[2]))

    def test_square(self):
        my_list = read('/src/Unit_Test_Square.csv')
        for row in my_list:
            self.assertEqual(self.calculator.squ(int(row[0])), int(row[1]))

    def test_squareroot(self):
                my_list = read('/src/Unit_Test_Squareroot.csv')
                for row in my_list:
                    self.assertEqual(self.calculator.sqr(int(row[0])), Decimal(row[1]))

if __name__ == '__main__':
    unittest.main()