#!/usr/local/bin/python3
# check for duplicates in a list

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
second_list = []
diff = []


def funct_duplicate():
    for letter in my_list:
        if letter not in second_list:
            second_list.append(letter)
        else:
            diff.append(letter)
    print(diff)


def funct_duplicates2():
    for letter in my_list:
        if my_list.count(letter) > 1:
            if letter not in diff:
                diff.append(letter)
    print(diff)


if __name__ == "__main__":
    print('Running Solution 1')
    funct_duplicate()
    print('Running Solution 2')
    funct_duplicates2()
