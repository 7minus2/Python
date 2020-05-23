#!/usr/local/bin/python3
from time import time
from translate import Translator


def myTimerFunction(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        return result, t1, t2
    return wrapper


@myTimerFunction
def fileTranslator(file, lang='ja', mode='r'):
    translator = Translator(lang)
    try:
        with open(file, mode) as my_file:
            lines = my_file.readlines()
    except FileNotFoundError as err:
        print('Unable to locate file')
    Translation_list = []
    for line in lines:
        print(line, translator.translate(line))
        Translation_list.append(translator.translate(line))
    return Translation_list


if __name__ == '__main__':
    result, t1, t2 = fileTranslator(file='../files/test.txt')
    print(result)
    print(f'It took {t2-t1} secs to translate')
