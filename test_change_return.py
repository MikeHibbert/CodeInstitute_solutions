import unittest

from change_return import give_change


class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02], 'wrong change given')
        self.assertEqual(give_change(.18), [.10, .05, .02, .01], 'wrong change given')

    def test_multiple_same_coins(self):
        self.assertEqual(give_change(.04), [.02, .02])
