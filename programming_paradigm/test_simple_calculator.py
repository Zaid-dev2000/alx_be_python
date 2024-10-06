import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(100, 50), 50)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 1), 3)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        
        # Test for division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None.")
        self.assertIsNone(self.calc.divide(0, 0), "0/0 should return None.")

    def test_edge_cases(self):
        """Test edge cases for all methods."""
        # Test large numbers
        self.assertEqual(self.calc.add(1e6, 1e6), 2e6)
        self.assertEqual(self.calc.subtract(1e6, 1e5), 9e5)
        self.assertEqual(self.calc.multiply(1e6, 2), 2e6)
        self.assertEqual(self.calc.divide(1e6, 2), 5e5)

if __name__ == "__main__":
    unittest.main()
