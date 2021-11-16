### Task 1.1
## Convert seconds to days, hours, minutes and seconds depends of the duration

duration = int(input('Duration: '))

sec = duration % (24 * 3600)    #convert input seconds to the 24 hour format
hour = sec // 3600     #1 hour is equivalent to 3600
sec = sec % 3600     #
min = sec // 60     #1 min is equivalent to 60 seconds
sec = sec % 60
day = duration // 86400
sec = sec % 86400

#result = '() hours, () minutes, () seconds'.format(hour, min, duration)

#print(hour, min, duration)

print(day + 's', hour + '', min, sec)


## print(f"")