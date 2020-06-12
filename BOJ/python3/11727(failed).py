n = int(input())

result = [0, 1, 3]

if n == 1:
    print(result[1])
elif n == 2:
    print(result[2])
else:
    for i in range(3, n+1):
        result.append(result[i-1] + result[i-2]*2)
    print(result[n] % 10007)
