import unittest

from change_return import give_change, give_item_and_change


class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02], 'wrong change given')
        self.assertEqual(give_change(.18), [.10, .05, .02, .01], 'wrong change given')

    def test_multiple_same_coins(self):
        self.assertEqual(give_change(.04), [.02, .02])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the
        item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0.5)
