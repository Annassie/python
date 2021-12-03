# Modify the previous function into num_translate_adv():
# implement correct work with numbers starting with a capital letter
# the result must also be capitalized


def num_translate_adv(num):
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

    for num in eng_rus:
        if num.title():
            print(eng_rus.get(num.title()))
        else:
            print(eng_rus.get(num))

    #print(eng_rus.get(num))


num_translate_adv("zero")








