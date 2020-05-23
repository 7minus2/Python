#!/usr/local/bin/python3


class User():
    """
    Dummy sign in message
    """

    def sign_in(self):
        print('User is logged in')


class Wizard(User):
    """
    Character: Wizard
    Traits: Magic Attack power
    """

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    """
    Character: Archer
    Traits: Run or Attack with arrows
    """

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} arrows remaining~')

    def run(self):
        print(f'Ran really fast')


class HybridBorg(Wizard, Archer):
    """
    HybridBorg has both Wizard + Archer character traits
    """

    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


if __name__ == "__main__":
    hb1 = HybridBorg('borgbot1', 50, 70)
    print('borgbot1: ', end='')
    print(hb1.sign_in())
    print('borgbot1: ', end='')
    print(hb1.attack())
