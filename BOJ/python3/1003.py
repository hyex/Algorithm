# 1. 이차원 배열으로 해결해보려 함 -> 런타임 에러

# t = int(input())
#
# arr = [[1, 0], [0, 1]]
# for _ in range(t):
#     n = int(input())
#     leng = len(arr)
#     if leng >= n:
#         print(*arr[n])
#     else:
#         while leng <= n:
#             arr.append([arr[leng-1][1], sum(arr[leng-1])])
#             leng += 1
#         print(*arr[n])

# 2. 규칙을 찾아 이용 -> 성공

t = int(input())

arr = [0, 1]
for _ in range(t):
    n = int(input())
    leng = len(arr)
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    elif leng >= n:
        print(arr[n-1], arr[n-1] + arr[n-2])
    else:
        while leng <= n:
            arr.append(arr[leng - 1] + arr[leng - 2])
            leng += 1
        print(arr[n-1], arr[n-1] + arr[n-2])
