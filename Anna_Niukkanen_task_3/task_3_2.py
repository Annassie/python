# Write the function, which returns numbers 0-10 from Enlgish to Russian.

from random import choice

def num_translate(num):
    eng_rus = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'four',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    return eng_rus.get(num, None)
  #  print(num["one"])


num_translate('one')