import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_sum(self):
        result = calculator.add(10, 10)
        self.assertEqual(result, 20)
        result = calculator.add(100, 100)
        self.assertEqual(result, 200)
        result = calculator.add(50, 50)
        self.assertEqual(result, 100)

    def test_sub(self):
        result = calculator.sub(10, 10)
        self.assertEqual(result, 0)
        result = calculator.sub(20, 10)
        self.assertEqual(result, 10)
        result = calculator.sub(30, 10)
        self.assertEqual(result, 20)

    def test_div(self):
        result = calculator.div(10, 5)
        self.assertEqual(result, 2)
        result = calculator.div(20, 5)
        self.assertEqual(result, 4)
        result = calculator.div(16, 4)
        self.assertEqual(result, 4)

    def test_mult(self):
        result = calculator.mult(10, 10)
        self.assertEqual(result, 100)
        result = calculator.mult(2, 6)
        self.assertEqual(result, 12)
        result = calculator.mult(32, 12)
        self.assertEqual(result, 384)