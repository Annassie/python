num = list(range(1, 101))

singular = ['процент']
declension = []


for i in range(0, len(num)):
    singular = list(num[i])
    if num == 1 and (num % 10 == 1):
        print(singular)
    elif num > 1 and num < 5 and (num % 10 == 3, 4, 5):
        singular.append('а')
    else:
        singular.append('ов')

    declension.append(singular)

print(declension)