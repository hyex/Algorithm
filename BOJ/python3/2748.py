# 1. 재귀함수로 풀이 -> 시간초과

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)


# n = int(input())
# print(f(n))

# 2. 배열에 append -> 성공

n = int(input())
arr = [0, 1]
for i in range(2, n+1):
    arr.append(arr[i-1]+arr[i-2])

print(arr[n])
