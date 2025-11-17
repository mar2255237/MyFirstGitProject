import unittest

# Function to test
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# ---------------------------
# Example Usage (normal output)
# ---------------------------
print("Example Usage:")
print("10 / 2 =", divide(10, 2))

try:
    print("10 / 0 =", divide(10, 0))
except ValueError as e:
    print("Error:", e)

print("\n")  # Blank line before tests run

# ---------------------------
# Unit Tests
# ---------------------------
class TestMathOperations(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # Correct result
        self.assertRaises(ValueError, divide, 10, 0)  # Correctly raises error

if __name__ == "__main__":
    unittest.main()
