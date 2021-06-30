import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
    '''''''''
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)
    '''''''''
    def test_add(self):
        result = Calculator.add(10, 5)
        self.assertEqual(result ,15)

    def test_minus(self):
        result = Calculator.minus(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = Calculator.multiply(20, 2)

    def test_divide(self):
        result = Calculator.divide(3, 2)
        self.assertEqual(result, 1)


if __name__ ==  '__main__':
    unittest.main()