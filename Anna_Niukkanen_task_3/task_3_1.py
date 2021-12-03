# Write the function, which returns numbers 0-10 from Enlgish to Russian.


def num_translate(num):
    eng_rus = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    print(eng_rus.get(num))


num_translate("three")





