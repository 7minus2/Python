#!/usr/local/bin/python3

# Rules: paramaters, *args, default paramaters, ***kwargs
# example:  function(name, *args, num=2, **kwargs)


def sum(num1, num2):
    '''
    Info: This adds 2 numbers \n
    Example: sum(1,2) returns 3
    '''
    return num1 + num2


def my_sum2(*args, **kwargs):
    '''
    Info: *args accepts multiple values as tuple (1,2,3,4,5) \n
    **kwargs needs num1 and num2 for sum() function
    '''
    total = 0
    print(f'args {args} kwargs: {kwargs}', end='\n')
    for item in args:
        total += item
    return total + sum(**kwargs)


if __name__ == "__main__":
    print(my_sum2(1, 2, 3, 4, 5, num1=5, num2=10))
