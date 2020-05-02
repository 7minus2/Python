#!/usr/local/bin/python3

"""
Users can be, but they have to b signed in first
- wizards
- archers
- ogres
Polymorphism, redefine methods
"""


class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_of_arrows}')


# isinstance(instance, Class)
wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 30)


def player_attack(char):
    char.attack()


if __name__ == '__main__':
    player_attack(wizard1)
    for char in [wizard1, archer1]:
        char.attack()
    print(isinstance(wizard1, Wizard))  # returns True
    print(isinstance(wizard1, object))  # returns True
