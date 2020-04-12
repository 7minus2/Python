#!/usr/local/bin/python3
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
from time import time
user1 = {
    'name': 'Cloud',
    'valid': True,  # changing flag will run/stop message_friends function.
    'id': 7
}


def authenticated(fn):
    '''
    INFO: Function to be used for decorator. \n
    Sends message, if user has True Value \n
    Usage: True for sending message/ False for not sending
    '''
    def wrapper1(*args, **kwargs):
        t1 = time()
        result = {key: value for (
            key, value) in args[0].items() if args[0].get('valid') == True}
        if len(result) != 0:
            result2 = fn(*args, **kwargs)
        t2 = time()
        print(f'Solution 1 took {t2-t1} s')
        return result2
    return wrapper1


def authenticated2(fn2):
    def wrapper2(*args, **kwargs):
        t1 = time()
        if args[0].get('valid'):
            result3 = fn2(*args, **kwargs)
        t2 = time()
        print(f'Solution 2 took {t2-t1} s')
        return result3
    return wrapper2


@authenticated
@authenticated2
def message_friends(user):
    '''
    INFO: send message if user is valid
    '''
    print('message has been sent')


if __name__ == '__main__':
    message_friends(user1)
