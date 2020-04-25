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


@func_timer
def func_problem7():
    '''
    INFO: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
    The element value in the i-th row and j-th column of the array should be i * j.
    Note: Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
    '''
    num1_input, num2_input = map(int, input(
        'Please enter 2 numbers by comma: ').split(','))
    result = []
    for num1 in range(num1_input):
        temp_num_holder = []
        for num2 in range(num2_input):
            temp_num_holder.append(num1*num2)
            # print(f'Temp number Value: {temp_num_holder}')
        result.append(temp_num_holder)
        # print(f'Current result Value is: {result}')
    # print(f'Final result Value is: {result}')
    return result


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

    print('Running Problem 4')
    result, timer1, timer2 = func_problem7()
    print(f'Solution is: {result}\n')
    print(f'It took {timer2-timer1} secs\n')
