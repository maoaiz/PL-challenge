"""
The goal of this exercise is to assess debugging.

Please read the comments in the following code, write a test to reproduce the error and fix the bug.

For this exercise, answers with another language are not permitted.
"""

import unittest


class OutOfOrderError(Exception):
    pass


class VendingMachine:
    """The vending machine can be filled using the add_item() method and a user can buy things from it
    using the buy_item() method.
    The buy_item() returns an item unless it's out of stock, in which case it raises an OutOfOrderError exception
    """

    def __init__(self):
        self.stock = []

    def _accept_orders(self):
        return bool(self.stock)  # or len(self.stock) > 0

    def add_item(self, item):
        self.stock.append(item)

    def buy_item(self):
        if self._accept_orders():
            return self.stock.pop(0)
        else:
            raise OutOfOrderError()

    def __str__(self):
        return "Insert coin" if self._accept_orders() else "Out Of Order"


class VendingMachineTests(unittest.TestCase):
    def test_out_of_stock(self):
        machine = VendingMachine()
        with self.assertRaises(OutOfOrderError):
            machine.buy_item()

    def test_buy_item(self):
        machine = VendingMachine()
        machine.add_item('ice cream')
        self.assertEqual(machine.buy_item(), 'ice cream')

    def test_buy_item_bug(self):
        """While checking the logs of your application, you've noticed an unexpected error and the following
        stack trace:

        Traceback (most recent call last):
          File "testing_and_debugging_2.py", line 60, in test_buy_item_bug
            self.assertEqual(machine.buy_item(), 'ice cream')
          File "testing_and_debugging_2.py", line 23, in buy_item
            return self.stock.pop(0)
        IndexError: pop from empty list

        Write the test to reproduce this error and fix the VendingMachine code
        """
        machine = VendingMachine()

        with self.assertRaises(OutOfOrderError):
            machine.buy_item()


if __name__ == '__main__':
    unittest.main()
