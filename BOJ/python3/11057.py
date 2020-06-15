N = int(input())

dp = [[0]*11 for _ in range(1001)]

for i in range(0, 10):
    dp[1][i] = 1
    dp[2][i] = 10-i

dp[1][10] = sum(dp[1])
dp[2][10] = sum(dp[2])


for i in range(3, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][10]
        else:
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
    dp[i][10] = sum(dp[i])

print(dp[N][10] % 10007)


