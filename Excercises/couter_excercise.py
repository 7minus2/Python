#!/usr/local/bin/python3

# counter exercise, return sum of my_list
# my_list = [1,2,3,4,5,6,7,8,9,10]


def counter_checker1(num):
    # Solution 1
    try:
        my_list = sum([x for x in range(1, int(num), 1)])
        return my_list
    except ValueError as err:
        return err


def counter_checker2(num):
    # Solution 2
    total_sum = 0
    for num in range(1, num, 1):
        total_sum += num
    return total_sum


if __name__ == '__main__':
    solution1 = counter_checker1('')
    print(f'Solution 1 Sum is: {solution1}', end='\n')  # Answer = 55
    solution2 = counter_checker2(11)
    print(f'Solution 2 Sum is: {solution2}', end='\n')  # Answer = 55
    print("All done!")
