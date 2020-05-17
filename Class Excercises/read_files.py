#!/usr/local/bin/python3
from time import time


def my_timer_func(fn):
    def wrapper(*args, **kwargs):
        timer1 = time()
        result = fn(*args, **kwargs)
        timer2 = time()
        return result, timer1, timer2
    return wrapper


@my_timer_func
def reviewTestFile(file, mode):
    my_file = open(file=file, mode=mode)
    print(my_file.read())
    my_file.close()


if __name__ == '__main__':
    print('Running Solution')
    func, timer1, timer2 = reviewTestFile(file='../files/test.txt', mode='r')
    print(f'It took {timer2 - timer1} secs')
