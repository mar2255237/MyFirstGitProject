import unittest

# Function to test
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

class TestMathOperations(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # Checking equality
        self.assertRaises(ValueError, divide, 10, 0)  # Checking error for division by zero

if __name__ == "__main__":
    unittest.main()
