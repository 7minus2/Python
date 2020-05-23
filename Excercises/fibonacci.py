#!/usr/local/bin/python
from time import time


def fun_timer(fn):
    def wrapper(*args, **kwargs):
        timer1 = time()
        run_func = fn(*args, **kwargs)
        timer2 = time()
        return run_func, timer1, timer2
    return wrapper


@fun_timer
def fibonacci(item):
    prev_num = 0
    nex_num = 1
    for i in range(item):
        yield prev_num
        temp_prev_num = prev_num
        prev_num = nex_num
        nex_num = temp_prev_num + nex_num


@fun_timer
def fib_list(item):
    prev_num = 0
    nex_num = 1
    num_list = []
    for i in range(item):
        num_list.append(prev_num)
        temp_prev_num = prev_num
        prev_num = nex_num
        nex_num = temp_prev_num + nex_num
    return num_list


if __name__ == '__main__':
    run_func, timer1, timer2 = fibonacci(10000)
    print('Running Solution 1')
    print(list(run_func))
    print(f'It took {timer2 - timer1} secs')

    run_func2, new_timer_1, new_timer2 = fib_list(10000)
    print('Running Solution 2')
    print(run_func2)
    print(f'It took {new_timer2-new_timer_1}')
