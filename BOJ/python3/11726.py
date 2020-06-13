n = int(input())

arr = [0, 1, 2]

for x in range(3, n+1):
    arr.append(arr[x-1]+arr[x-2])

print(arr[n] % 10007)
