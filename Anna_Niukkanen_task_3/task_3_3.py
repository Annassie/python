# Write a thesaurus()-function that takes employee's names as arguments
# and returns a dictionary in which the keys are the first letters of the names
# and the values are lists containing names starting with the corresponding letter
# For example:
# >>> thesaurus ("Ivan", "Maria", "Peter", "Ilya")
# {
#      "And": ["Ivan", "Ilya"],
#      "M": ["Mary"], "P": ["Peter"]
# }


#keys_in_dict = []


def thesaurus(*names):
    dict_names = {}
    # for name in names:
    #     char = name[0]
    #     if char in dict_names:
    #         dict_names[char].append(name)
    #     else:
    #         dict_names[char] = [name]
    # return dict_names

    for name in names:
        if name[0] not in dict_names.keys():
            dict_names[name[0]] = name          ## taking index #0 of the name
            #dict_names.setdefault(name[0])

           # dict_names[name[0]].setdefault(name)
        else:
            if name not in dict_names[name[0]]:
                #dict_names.setdefault(name)
               print(False)
              #  dict_names[name[0]].append(name)

    for key, val in dict_names.items():
        print(key, ':', val)




print(thesaurus("Ivan", "Maria", "Peter", "Ilya"))



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
