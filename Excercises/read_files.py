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
    my_file = open(file, mode)
    print(my_file.read())
    my_file.close()


@my_timer_func
def reviewTestFile2(file, mode):
    try:
        with open(file, mode) as my_file:
            if 'a+' in mode:
                my_file.write('New line Added\n')
                my_file.seek(0)
            print(my_file.readlines())
    except FileNotFoundError as err:
        print('File can\'t be found')
    except IOError as err:
        print('IO error')
        raise err


if __name__ == '__main__':
    print('Running Solution 1')
    func, timer1, timer2 = reviewTestFile(file='../files/test.txt', mode='r')
    print(f'It took {timer2 - timer1} secs')

    print('Running Solution 2')
    func2, timer1, timer2 = reviewTestFile2(
        file='../files/test.txt', mode='a+')
    print(f'It took {timer2 - timer1} secs')
