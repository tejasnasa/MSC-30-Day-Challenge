import calendar

s = input()

m = int(s[0:2])
d = int(s[3:5])
y = int(s[6:])

print(calendar.day_name[calendar.weekday(y, m, d)].upper())
