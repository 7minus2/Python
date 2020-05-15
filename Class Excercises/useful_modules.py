#!/usr/local/bin/python3
from collections import Counter, defaultdict, OrderedDict


# creates a dict of how many times number occurs in a iterable
li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = "Something jumped over the sheet"

# this helps count like dup emails or users for example
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})


# retains the order it was created
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2


if __name__ == "__main__":
    print(Counter(li))
    print(Counter(sentence))
    print(dictionary['c'])
    # normal dictionary would be false, python3.7 + newer has ordered dict by default
    print(d2 == d)  # true
