### Task_2_2
# Is given list:
# ['at', '5', 'hours', 'and', '17 minutes', 'o'clock', 'the air', 'temperature', 'was', '+5', 'degrees']
# handle the list so, than every number has quotation marks (" ") and add 0 to numbers than number has two integer values.
# ['at', '"', '05', '"', 'hours', 'and', '"', '17 minutes', '"', 'o'clock', 'the air', 'temperature', 'was', '"', '+05', '"', 'degrees']
# and get from list the string:
# at "05" hours and "17" minutes the air temperature was "+05" degrees

raw_list = ['at', '5', 'hours', 'and', '17', 'minutes', 'o\'clock', 'the air', 'temperature', 'was', '+5', 'degrees']
#raw_message = ['5']
print(raw_list)
print(id(raw_list))

new_list = []

for item in raw_list:
    if item.isnumeric():
        item = item.zfill(2)
        #new_list.append('"' + item + '"')
        new_list.append('"')
    elif item.lstrip('+').isnumeric():
        item = item.zfill(3)
        new_list.append('"')
    new_list.append(item)
print(new_list)
print(id(new_list))

string_from_list = ' '.join(new_list)
print(string_from_list)

# string_from_list = ''
# for item in new_list:
#     string_from_list += item
#     string_from_list += ' '
# print(string_from_list)


