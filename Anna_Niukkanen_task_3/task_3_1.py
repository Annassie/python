# Write the function, which returns numbers 0-10 from Enlgish to Russian.


def num_translate(num):
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

num_translate(eng_rus.get("two"))





# Solution #2

# def num_translate_adv(num):
#     eng_rus = {
#         'zero': 'ноль',
#         'one': 'один',
#         'two': 'два',
#         'three': 'три',
#         'four': 'four',
#         'five': 'пять',
#         'six': 'шесть',
#         'seven': 'семь',
#         'eight': 'восемь',
#         'nine': 'девять',
#         'ten': 'десять',
#     }
#     return eng_rus.get(num, None)
#
#
# print(num_translate_adv('two'))