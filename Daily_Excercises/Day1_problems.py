#!/usr/local/bin/python3
import math


def prob1_solution(num1, num2):
    '''
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
    '''
    prob1_solution = [num for num in range(
        num1, num2+1, 1) if (num % 7 == 0) and (num % 5 != 0)]
    return prob1_solution


def prob2_solution():
    '''
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output should be:40320
    1*2*3*4*5*6*7*8 = 40320
    '''
    while True:
        try:
            question = int(input('Please enter a number: '))
            break
        except Exception as err:
            print(f'You need to enter a valid number \n Error: {err}')
            continue
    return math.factorial(question)


def prob3_solution():
    '''With a given integral number n, 
    write a program to generate a dictionary that contains (i, i x i) 
    such that is an integral number between 1 and n (both included). 
    and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
    '''
    while True:
        try:
            result = int(
                input('Please enter a number to generate dict list n:n*n :'))
            num_dict = {x: x*x for x in range(1, result+1)}
            break
        except Exception as err:
            print(f'You need to enter an integer Sir! \n Error: {err}')
            continue
    return num_dict


if __name__ == '__main__':
    print('Running Solution 1')
    print(prob1_solution(2000, 3200))

    print('Running Solution 2')
    print(prob2_solution())

    print('Running Solution 3')
    print(prob3_solution())
    print('Prgram has ended')
