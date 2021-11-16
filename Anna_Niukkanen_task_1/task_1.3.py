# Realise declension of the word "percent" in phrase "N percents"
# And print this phrase on a separate line for each of numbers
# in range from 1 to 100

for idx in range(1, 101):
    if idx == 1 or idx % 10 == 1:
        print(idx, 'процент')
    elif 2 <= idx <= 4 or idx % 10 == 2 or idx % 10 == 3 or idx % 10 == 4:
        print(idx, 'процента')
    else:
        print(idx, "процентов")
