#!/usr/local/bin/python3


class Cat():
    species = 'mamal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
cat1 = Cat('Tigger', 1)
cat2 = Cat('Smokey', 4)
cat3 = Cat('Patch', 10)


def oldest_cat(*args):
    '''
    INFO: Create a function that finds the oldest cat
    '''
    return max(args)


if __name__ == '__main__':
    # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function
    print(f'The oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)}')
