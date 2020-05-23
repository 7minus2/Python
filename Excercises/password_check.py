#!/usr/local/bin/python3


def pass_length_checker():
    print('Welcome to password length checker \n Please enter you\'re username + password!')
    username = input('Username: ')
    password = input('Password: ')
    encrypt_pass = int(len(password)) * 'x'
    pass_length = len(password)

    print(f'{username}, you\'re password {encrypt_pass} is {pass_length} letters long')


if __name__ == '__main__':
    pass_length_checker()
