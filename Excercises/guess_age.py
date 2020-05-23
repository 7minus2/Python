import datetime


def age():
    birth_year = int(input('What year were you born?\n'))
    now = int(datetime.datetime.now().strftime('%Y'))
    age = now - birth_year

    print(f'You are {age} years old!')


if __name__ == "__main__":
    age()
