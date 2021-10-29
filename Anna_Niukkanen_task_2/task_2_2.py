### Task_2_2
# Is given list:
# ['at', '5', 'hours', 'and', '17 minutes', 'o'clock', 'the air', 'temperature', 'was', '+5', 'degrees']
# handle the list so, than every number has quotation marks ("") and add 0 than number has two integer values.
# ['at', '""', '05', '""', 'hours', 'and', '""', '17 minutes', '""', 'o'clock', 'the air', 'temperature', 'was', '""', '+05', '""', 'degrees']
# and get from list the string
# at "05" hours and "17" minutes the air temperature was "+05" degrees

raw_list = ['at', '5', 'hours', 'and', '17', 'minutes', 'o\'clock', 'the air', 'temperature', 'was', '+5', 'degrees']
#raw_message = ['5']
print(raw_list)
print(id(raw_list))
new_list = []  # define a new list
for item in raw_list:
 #   print(type(item))
    num = ''
    if num == item.isnumeric:
        print(num)
 # check if str is number
 #   num_2 = '""'.join(num)
#    if num == item.isnumeric() and num < 10:
#        num = '0' + str(num)
  #  new_list += [item]
    if num == item.isnumeric() and num < 10:
        res_num = item.zfill(2)

#    if num < 10:
    new_list += [item]     # adding leading zero to the number
#    elif num > 10:
#        new_list += [item.zfill(4)]


#       num = '""'.join('"' + num + '"' for num in raw_message)
#print(new_list)
#print(type(item))
#print(id(new_list))



#print(type(raw_message[1])) ## str

#message = ' '.join(raw_message)
#print(message)

### Another method to join elements of list, but it doesn't work with isnumeric()
#message = ''
#for item in raw_message:

#    message += item
#    message += ' '
#    print(item.zfill(2))
#print(message)



#num = '""'.join('"' + item + '"' for item in message)

#print(num)