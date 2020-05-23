#!/usr/local/bin/python3
import unittest
from Excercises.highest_even import highest_even
from Excercises.couter_excercise import counter_checker1, counter_checker2


class TestMain(unittest.TestCase):
    def test_highest_even(self):
        my_list = [10, 2, 3, 4, 8, 11]
        result = highest_even(my_list)
        self.assertEqual(result, 10)

    def test_counter(self):
        num = 11
        result = counter_checker1(num)
        self.assertEqual(result, 55)

    def test_counter1(self):
        num = ''
        result = counter_checker1(num)
        self.assertIsInstance(result, ValueError)

    def test_counter1b(self):
        num = 'straasdf'
        result = counter_checker1(num)
        self.assertIsInstance(result, ValueError)

    def test_counter2(self):
        num = 12
        result = counter_checker2(num)
        self.assertEqual(result, 66)


if __name__ == '__main__':
    unittest.main()
