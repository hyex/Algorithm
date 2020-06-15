N = int(input())

dp = [0, 1]

for x in range(2, N+1):
    dp.append(dp[x-1] + dp[x-2])

print(dp[N])

