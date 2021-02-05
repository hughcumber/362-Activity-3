import unittest
import calculator

if __name__ == "__main__":
    unittest.main(verbosity=2);


def test_addition(self):
    result = addition(10, 5);

    self.assertEqual(result, 15);


def test_subtraction(self):
    result = subtraction(10, 5);

    self.assertEqual(result, 5);


def test_multiplication(self):
    result = multiplication(10, 5);

    self.assertEqual(result, 50);


def test_division(self):
    result = division(10, 5);

    self.assertEqual(result, 2);
