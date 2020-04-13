#!/usr/local/bin/python3
from time import time


def func_timer(fn):
    def wrapper(*args, **kwargs):
        timer1 = time()
        result = fn(*args, **kwargs)
        timer2 = time()
        return result, timer1, timer2
    return wrapper


@func_timer
def genator_for_loop(item):
    item = iter(item)
    while True:
        try:
            print(f'Generator in memory location: {item}')
            print(f'Value is: ', next(item))
        except StopIteration:
            print(f'No More iteration: Exiting!!!')
            break


if __name__ == '__main__':
    result, timer1, timer2 = genator_for_loop([1, 2, 3])
    print(result)
    print(f'It took {timer2-timer1} secs to run')
