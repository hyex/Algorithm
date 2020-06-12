n = int(input())

for star in range(n, 0, -1):
    print(" "*(n-star) + "*"*star)
