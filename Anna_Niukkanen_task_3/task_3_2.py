# Modify the previous function into num_translate_adv():
# implement correct work with numbers starting with a capital letter
# the result must also be capitalized


def num_translate(num):
    # for num in eng_rus:
    #     if num.title():
    #        # num[val].title()
    #         eng_rus[num] = num.title()
    #         print(f"{num.title()}")
    #     else:
    #         print(f"{num}")
    # for element in num:
    #     if element.title():
    #         print(f"{element.title()}")
    #     else:
    #         print(f"{element}")
    if num.title():
        print(f"{num.title()}")
    else:
        print(f"{num}")


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


num_translate(eng_rus.get("ten"))
