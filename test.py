#!/usr/local/bin/python3
import unittest
from Excercises.highest_even import highest_even
from Excercises.couter_excercise import counter_checker1, counter_checker2
from Excercises.random_guessing_game import rand_game
import sys
from mock import patch


class TestMain(unittest.TestCase):

    int_num = 12

    def setUp(self):
        print('Running Test')

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
        result = counter_checker2(self.int_num)
        self.assertEqual(result, 66)

    def test_counter2(self):
        result = counter_checker2(self.int_num)
        self.assertEqual(result, 66)

    @patch('builtins.input', lambda * args: 1)
    def test_guessing_game(self):
        sys.argv = [None, 1, 12, 2]
        result = rand_game(sys.argv[1], sys.argv[2], sys.argv[3])
        self.assertEqual(result, 1)

    def tearDown(self):
        print('Cleaning Up')


if __name__ == '__main__':
    unittest.main(verbosity=2)
