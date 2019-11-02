import unittest
from Calculator import Calculator
from CSVReader import read

class MyTestCase(unittest.TestCase):
    calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        my_list=read('/src/Unit_Test_Addition.csv')
        for row in my_list:
         self.assertEqual(self.calculator.add(int(row[0]),int(row[1])), int(row[2]))

if __name__ == '__main__':
    unittest.main()