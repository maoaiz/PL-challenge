"""
The goal of this exercise is to assess unit testing.

You are asked to write 3 tests for the division operator in the language of your choice.

The following code is provided as a Python 3 example of how to write unit tests.

You can add your answers to the DivisionTests class.

If you use another language, please provide instructions to run the script.
"""

import unittest


class AdditionTests(unittest.TestCase):
    """This is a test example for the addition (+) operator
    """

    def test_addition_integer(self):
        self.assertEqual(1 + 1, 2)


class DivisionTests(unittest.TestCase):
    """
    Write at least three tests to verify the behavior of the division (/) operator
    """

    def test_black_box(self):
        self.assertEqual(10 / 2, 5)

    def test_invalid_params(self):
        with self.assertRaises(TypeError):
            10 / '2'

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            10 / 0

    def test_division_by_zero2(self):

        with self.assertRaises(ZeroDivisionError) as e:
            10 / 0

        self.assertEqual(
            'division by zero',
            str(e.exception)
        )


if __name__ == '__main__':
    unittest.main()
