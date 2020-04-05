#!/usr/local/bin/python3


def checkDriverAge(age=0):
    # if not age:
    #     age = int(input('What is your age?: '))
    if int(age) < 18:
        print('Sorry, you are too young to drive this car '
              'Powering off!')
    elif int(age) > 18:
        print('Powering On. Enjoy the ride!')
    elif int(age) == 18:
        print('Congratulations on your first year of'
              'driving. Enjoy the ride')
    return age


if __name__ == "__main__":
    age = checkDriverAge(19)
    print(f'You\'re age is {age}')
