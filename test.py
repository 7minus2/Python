#!/usr/local/bin/python3
import unittest
from Excercises.highest_even import highest_even


class TestMain(unittest.TestCase):
    def test_highest_even(self):
        my_list = [10, 2, 3, 4, 8, 11]
        result = highest_even(my_list)
        self.assertEqual(result, 10)


unittest.main()
