#!/usr/local/bin/python3
import sys
import random


def rand_game(first_number, second_number, seed):
    '''
    INFO: Guess a number based on 2 different integers
    Example: random_game.py <number1> <number2> <seed>
    '''
    random.seed(seed)
    rand_number = random.randint(first_number, second_number)
    while True:
        try:
            input_number = int(
                input(f'Please guess a number between {first_number} and {second_number}:\n'))
            if input_number == rand_number:
                print(f'You win Sir!!\n')
                return rand_number
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
    rand_game(1, 10, 2)
# else:
#     first_number = sys.argv[1]
#     second_number = sys.argv[2]
#     seed = sys.argv[3]
#     rand_game(first_number, second_number, seed)
