#!/usr/local/bin/python3
from time import time


def func_timer(fn):
    def wrapper(*args, **kwargs):
        timer1 = time()
        result = fn(*args, **kwargs)
        timer2 = time()
        print(f'(It took {timer2-timer1} seconds to run')
        return result
    return wrapper


@func_timer
def func_error():
    while True:
        try:
            age = int(input('What is your Age Sir/Madam?'))
            10/age
            print(f'You\'re age is {age}')
        except (ValueError, ZeroDivisionError) as err:
            print(f'Please enter an integer greater than 0!\nError is: {err}')
            continue
        else:
            print('Thank you for your input, Program Exiting')
            break
        finally:
            print('Function is done running')


if __name__ == '__main__':
    func_error()
