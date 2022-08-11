sec = int(input("Input seconds: "))

day = sec // 86400
sec -= 86400 * day
hour = sec // 3600
sec -= 3600 * hour
min = sec // 60
sec -= 60 * min

print("The time passed is " + str(day) + " day(s):" + str(hour) + " hr(s):" + str(min) + " min(s):" + str(sec) + " sec(s)")
