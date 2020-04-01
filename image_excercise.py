#!/usr/bin/local/python3

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# 0 = empty space 1 = *
pixel = '*'
space = ' '


def tree():
    for index, num in enumerate(picture):
        for n in num:
            if n:
                print(pixel, end=' ')
            else:
                print(space, end=' ')
        print('')


if __name__ == "__main__":
    print('Solution: \n')
    tree()
