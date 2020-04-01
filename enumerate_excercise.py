#!/usr/local/bin/python3


def funct_number():
    for index, char in enumerate(list(range(0, 101, 1))):
        if char == 50:
            print(f'index is {index} character is {char}')


if __name__ == "__main__":
    funct_number()
