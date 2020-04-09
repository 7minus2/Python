#!/usr/local/bin/python3
from functools import reduce


def func_capital_word(words):
    '''
    INFO: Capitalize all of the pet names and print the list \n
    Usage: pass a list of words ['word', 'word2', 'word3']
    '''
    return words.upper()


def func_zip_lists(list1, list2):
    '''
    INFO: Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
    '''
    return zip(list1, list2)


def func_filter_scores(score):
    '''Filter the scores that pass over 50%
    '''
    return score > 50


def func_reduce_lists_combine(acc, number):
    '''
    INFO:Combine all of the numbers that are in a list on this file using reduce \n
    (my_numbers and scores). What is the total?
    '''
    return acc + number


if __name__ == '__main__':
    print('Running Solution for Capitalizing words', end='\n')
    print(list(map(func_capital_word,
                   ['sisi', 'bibi', 'titi', 'carla'])), end='\n\n')
    print('Running Solution for zipping lists', end='\n')
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [5, 4, 3, 2, 1]
    print(
        list(zip(func_zip_lists(my_strings, my_numbers))), end='\n\n')
    print('Running Solution for filtering a list of scores', end='\n')
    scores = [73, 20, 65, 19, 76, 100, 88]
    print(list(filter(func_filter_scores, scores)), end='\n\n')
    print('Running Solution for combining all numbers using reduce', end='\n')
    print(reduce(func_reduce_lists_combine, my_numbers + scores, 0))
