#!/usr/local/bin/python3


class Mygenerator():
    current_position = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if Mygenerator.current_position < self.last:
            num = Mygenerator.current_position
            Mygenerator.current_position += 1
            return num
        print('Iteration ended')
        raise StopIteration


gen = Mygenerator(0, 101)
print(gen)
for number in gen:
    print(number)
