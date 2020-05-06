#!/usr/local/bin/python3

# Problem 1: create a function that squares the list
my_list = [5, 4, 3]

# Problem 2: list sorting, sort based on 2nd value
my_list2 = [(0, 2), (4, 3), (9, 9), (10, -1)]


def func_square(item):
    '''
    INFO: Create a function to square the list
    '''
    return item ** 2


# lambda expression for problem 1
lambda item: item ** 2


def func_tuple_by_1st_item(item):
    '''
    INFO: Create a function to sort tuple by first item
    '''
    return item[0]


my_list2.sort(key=lambda k: k[0])


def func_tuple_by_2nd_item(item):
    '''
    INFO: Create a function to sort tuple by 2nd item
    '''
    return item[1]


my_list2.sort(key=lambda k: k[1])


if __name__ == '__main__':
    print('Problem 1 solution using a function')
    print(list(map(func_square, my_list)), end='\n\n')
    print('Problem 1 solution using lambda')
    print(list(map(lambda item: item ** 2, my_list)), end='\n\n')
    print('Problem 2 solution: sort by 1st item')
    print(sorted(my_list2, key=func_tuple_by_1st_item), end='\n\n')
    print('Problem 2 solution: sort by 2nd item')
    print(sorted(my_list2, key=func_tuple_by_2nd_item), end='\n\n')
    print('Problem 2 solution: sort by 1st item using lambda')
    my_list2.sort(key=lambda k: k[0])
    print(my_list2, end='\n\n')
    print('Problem 2 solution: sort by 1st item using lambda')
    my_list2.sort(key=lambda k: k[1])
    print(my_list2)
