# Create a list consisting numbers in cube of odd numbers (^3) between 1 and 1000
#
# a. define sum of numbers of the list, which sum is divisible by 7 completely (%)
# for example if number 19 ^ 3 = 6859, so sum of it is (6 + 8 + 5 + 9 = 28 ) / 7
# is divisible by 7 // use only math operations
#
# b. Add 17 to each element of the list, and define sum of numbers, which sum is divisible by 7
#
# *c. Solve task 2 without creating a new list.

#
num = []
for idx in range(1, 1000, 2):
    num.append(idx ** 3)
print(num, id(num))

# a.
new_list = []
for elem in num:
    sum = 0
    for digit in str(elem):
        sum += int(digit)
    if sum % 7 == 0:
        new_list.append(sum)
print(new_list, id(new_list))

# b.

new_list_2 = []
for element in num:
    sum_2 = 0
    new_num = element + 17
    for digit in str(new_num):
        sum_2 += int(digit)
    if sum_2 % 7 == 0:
        new_list_2.append(sum_2)
print(new_list_2, id(new_list_2))

# c. without creating a new list

for i in range(len(num)):
    sum_3 = 0
    num[i] = num[i] + 17
    for digit in str(num[i]):
        sum_3 += int(digit)
    if sum_3 % 7 == 0:
        num.append(sum_3)
print(num, id(num))



