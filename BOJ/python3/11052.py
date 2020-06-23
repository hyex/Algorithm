# 11052 중간에 졸아서 얼마나 걸린지 기억 안나지만 오래 걸리지 않음 주저리주저리

"""
10 9 8 7 6

카드 갯수 = 1 인 최대 값 dp[1]
P1 = 10
10

카드 갯수 = 2 인 최대 값 dp[2]
dp[1] + dp[1] = 20
dp[2] = 9
20

카드 갯수 = 3 인 최대 값 dp[3]
dp[1] + dp[2] = 30
dp[2] + dp[1] = 30 // 제외되면 좋을 듯
dp[3] = 8
30

카드 갯수 = 4 인 최대 값 dp[4]

"""
N = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
length = len(p) - 1
dp = [0] * (length+1)

dp[1] = p[1]

for i in range(2, length+1):
    money = 0
    for j in range(1, i+1):
        if j == i:
            if money < p[i]:
                money = p[i]
        elif money < dp[j] + dp[i-j]:
            money = dp[j] + dp[i-j]

    dp[i] = money

print(dp[length])
