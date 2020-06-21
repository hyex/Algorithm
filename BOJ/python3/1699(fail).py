N = int(input())
arr = [100000] * (N+1)
square = []

for i in range(N+1):
    x = i*i 
    if x > N:
        break
    square.append(x)
    arr[x] = 1

# print(arr)

for idx in range(N+1):
    for sq in square:
        # print("idx = ", idx, "sq = ", sq)
        if idx < sq:
            break
        # print("arr[idx] = ", arr[idx], " arr[sq] + arr[idx-sq] = ", arr[sq] + arr[idx-sq])
        arr[idx] = min(arr[idx], arr[sq] + arr[idx-sq])
        # print(arr[idx])

print(arr[N])
