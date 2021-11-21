### Task_2_4
# Given a list containing deformed data with positions and names of employees:
# ['design-engineer Igor', 'general accountant MARINA', 'mechanist of the highest category nIKOLAY', 'director of aelit']
# It's known that the name of employee is at the end of the line/string
# Generate and display phrases of the form "Hello Igor!"
# How to get the names of employees from the list items?
# and bring them to the correct form?
# Is it possible to avoid creating a new list?

# solving the problem
# 1) Get names from the list
# 2) Bring names to the correct form
# 3) Display phrases with the names
# 4) NOT to create a new list


employees = ['design-engineer Igor', 'general accountant MARINA', 'highest category mechanist nIKOLAY', 'director aelita']
print(employees, id(employees))

names = []
for item in employees:
    for element in item:
        reversed_list = item[::-1]
        rev_name = reversed_list[:reversed_list.index(' ')]
        name = rev_name[::-1]
    names.append(name.title())
print(names, id(names))

for name in names:
    greeting = f'Hi {name}!'
    print(greeting)

