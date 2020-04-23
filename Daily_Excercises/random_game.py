#!/usr/local/bin/python3
import sys
from random import randint

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])


def rand_game(first_number, second_number):
    '''
    INFO: Guess a number based on 2 different integers
    Example: random_game.py <number1> <number2>
    '''
    rand_number = randint(first_number, second_number)
    while True:
        try:
            input_number = int(
                input(f'Please guess a number between {first_number} and {second_number}:\n'))
            if input_number == rand_number:
                print(f'You win Sir!!\n')
                break
            elif input_number > second_number:
                print('Your number is out of range\n')
                continue
            elif input_number < rand_number:
                print(f'Hint: Guess a number higher than {input_number}\n')
                continue
            else:
                print(f'Hint: Guess a number lower than {input_number}\n')
                continue
        except Exception as err:
            print(f'Error has occured: {err}\n')
            continue


if __name__ == '__main__':
    rand_game(first_number, second_number)
