# Write a thesaurus()-function that takes employee's names as arguments
# and returns a dictionary in which the keys are the first letters of the names
# and the values are lists containing names starting with the corresponding letter
# For example:
# >>> thesaurus ("Ivan", "Maria", "Peter", "Ilya")
# {
#      "And": ["Ivan", "Ilya"],
#      "M": ["Maria"], "P": ["Peter"]
# }


def thesaurus(*names):
    dict_names = {}

    for name in names:
        if name[0] not in dict_names.keys():
            dict_names[name[0]] = []
            dict_names[name[0]].append(name)
        else:
            if name not in dict_names[name[0]]:
                dict_names[name[0]].append(name)

    for key, val in dict_names.items():
        print(key, ':', val)


thesaurus("Ivan", "Maria", "Peter", "Ilya")



# Without function
#
# names = ("Ivan", "Maria", "Peter", "Ilya")
#
# dict_names = {}
#
# for name in names:
#     if (name[0] not in dict_names.keys()):
#         dict_names[name[0]] = []
#         dict_names[name[0]].append(name)
#     else:
#         if (name not in dict_names[name[0]]):
#             dict_names[name[0]].append(name)
#
# print(dict_names)
