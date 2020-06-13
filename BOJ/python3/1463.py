n = int(input())

arr = [0, 0, 1]

for x in range(3, n+1):

    candidate = []
    if x % 3 == 0:
        candidate.append(x // 3)
    if x % 2 == 0:
        candidate. append(x // 2)
    candidate.append(x-1)
    if 1 in candidate:
        arr.append(1)
    else:
        minimum = 1000000
        while candidate:
            c = candidate.pop()
            if arr[c] < minimum:
                minimum = arr[c]
        arr.append(minimum + 1)


print(arr[n])
