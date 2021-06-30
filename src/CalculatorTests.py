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


if __name__ ==  '__main__':
    unittest.main()