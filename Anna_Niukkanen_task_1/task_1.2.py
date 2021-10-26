num = [i**3 for i in range(1, 1000, 2)]

#num = 4533

#n = len(arr)
sum = 0

while (num != 0):
    sum = sum + num % 10
    num = num // 10


print(sum)