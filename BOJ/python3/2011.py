# 2011 22:28 - 58 (30m)


"""
25114

길이 1
2
2 : 1

길이 2
25
1,2 / 12 = 2

if 조건 = 합쳐진 수가 27보다 작다면(26과 같거나 작다면)

길이 3
251
2, 5, 1 / 25, 1 / 2, 51 = 3
dp[3-2] && pw[3-1] + pw[3] 이 조건에 맞는 경우 + dp[3-1]


"""

pw = list(map(int, input()))
length = len(pw)
dp = [0] * (length+1)
dp[0] = 1
# if pw[1] == 0:
#     print("0")
#     exit()

for i in range(1, length+1):
    if 1 <= pw[i-1] <= 9:
        dp[i] = dp[i-1]
    if i == 1:
        continue
    num = pw[i-2]*10 + pw[i-1]
    if 10 <= num <= 26:
        dp[i] += dp[i-2]

# print(dp)
print(dp[length] % 1000000)
