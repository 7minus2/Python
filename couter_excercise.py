#!/usr/local/bin/python3

# counter exercise, return sum of my_list
# my_list = [1,2,3,4,5,6,7,8,9,10]


def counter_checker1():
    # Solution 1
    my_list = sum([x for x in range(11)])
    print(f'Solution 1 Sum is: {my_list}', end='\n')  # Answer = 55


def counter_checker2():
    # Solution 2
    total_sum = 0
    for num in range(11):
        total_sum += num
    print(f'Solution 2 Sum is: {total_sum}', end='\n')  # Answer = 55


if __name__ == '__main__':
    counter_checker1()
    counter_checker2()
    print("All done!")
