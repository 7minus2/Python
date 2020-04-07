#!/usr/local/bin/python3


def highest_even(my_list):
    '''
    Info: Get the highest even number from a list of numbers \n
    Example: highest_even([10,2,3,4,8,11]) # returns 10
    '''
    even_list = [num for num in my_list if num % 2 == 0]
    highest_number = sorted(even_list, reverse=True)
    return highest_number[0]


if __name__ == "__main__":
    print(highest_even([10, 2, 3, 4, 8, 11]))
