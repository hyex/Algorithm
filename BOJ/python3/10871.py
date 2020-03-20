N, X = map(int, input().split())
# list 
inArr = list(map(int, input().split()))

for i in range(N):
    if inArr[i] < X:
        print(inArr[i], end=" ")
print("")
