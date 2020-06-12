n = int(input())

if n == 1:
    print(" "*(n-1) + "*")
else:
    print(" "*(n-1) + "*")
    blank = 1
    for i in range(2, n):
        print(" "*(n-i) + "*" + " "*blank + "*")
        blank += 2

    print("*"*(2*n-1))
