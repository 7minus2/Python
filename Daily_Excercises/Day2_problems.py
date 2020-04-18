#!/usr/local/bin/python3
from time import time


def func_timer(fn):
    def wrapper(*args, **kwargs):
        timer1 = time()
        func_result = fn(*args, **kwargs)
        timer2 = time()
        return func_result, timer1, timer2
    return wrapper


@func_timer
def func_problem4():
    '''
    INFO: Write a program which accepts a sequence of comma-separated numbers
    from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:
    '''
    my_list = input('Please enter comma seperated numbers: \n'
                    'ie: 34, 67, 55, 33, 12, 98\n:')
    new_list = list(my_list.split(","))
    new_tuple = tuple(new_list)
    return new_list, new_tuple


class myproblem5():
    '''
    INFO: Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    '''

    def __init__(self):
        pass

    def getString(self):
        self.var_string = input('Please enter an input: ')
        return self.var_string

    def printString(self):
        return self.var_string.upper()


@func_timer
def func_problem6(*args, **kwargs):
    '''
    INFO: Write a program that calculates and prints the value according to the given formula
    Formula: Q = Square root of [(2 * C * D)/H]
    '''
    C = 50
    H = 30
    results = []
    for number in args:
        var_Q = int(((2 * C * number) / H) ** (1/2))
        results.append(var_Q)
    return results


if __name__ == '__main__':
    print('Runnign Problem 1')
    func_result, timer1, timer2 = func_problem4()
    print(f'List: {func_result[0]}\nTuple: {func_result[1]} ')
    print(f'It took {timer2-timer1} secs\n')

    print('Runnign Problem 2')
    input_string = myproblem5()
    print(f'String entered =  {input_string.getString()}')
    print(f'Printing string in uppercase: {input_string.printString()}')

    print('Runnign Problem 3')
    result, timer1, timer2 = func_problem6(100, 150, 180)
    print(f'Solution is: {result}\n')
    print(f'It took {timer2-timer1} secs\n')
