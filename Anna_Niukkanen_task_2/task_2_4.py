### Task_2_3
# Is given deformed list
# ['design-engineer Igor', 'general accountant MARINA', 'mechanist of the highest category nIKOLAY', 'director of aelit']
# It's known that names are in the end of the string
# Form and display sentences like "Hello Igor!"
# How to get the names of employees from the list?
# and get them in the correct form?
# Is it possible not to create a new list?

# solving the problem
# 1) get names from the list
# 2) bring names to the correct view
# 3) Display sentences with the names
# 4) NOT to create a new list


raw_list = ['design-engineer Igor', 'general accountant MARINA', 'mechanist of the highest category nIKOLAY', 'director of aelit']

for item in raw_list:
    names = raw_list.pop(::1)
    print(names)