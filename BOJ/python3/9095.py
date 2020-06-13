T = int(input())

arr = [0, 1, 2, 4]

for _ in range(T):
    n = int(input())
    length = len(arr)
    if n < length:
        print(arr[n])
    else:
        for x in range(length, n+1):
            arr.append(arr[x-1]+arr[x-2]+arr[x-3])
        print(arr[n])

