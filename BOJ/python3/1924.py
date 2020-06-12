x, y = map(int, input().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0

for i in range(1, x):
    days += month[i]

days += y - 1

days = days % 7

if days == 0:
    print("MON")
elif days == 1:
    print("TUE")
elif days == 2:
    print("WED")
elif days == 3:
    print("THU")
elif days == 4:
    print("FRI")
elif days == 5:
    print("SAT")
elif days == 6:
    print("SUN")
