case = int(input())
result = [0 for _ in range(case)]  # c
for c in range(case):
    m, n, k = map(int, input().split())
    inp = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        inp[y][x] = 1

    # 연산
    for i in range(n):
        for j in range(m):
            if inp[i][j] == 1:
                neighborhood = [[i, j]]
                inp[i][j] = 0
                while neighborhood:
                    one, two = neighborhood.pop()
                    if one != 0 and inp[one-1][two] == 1: # up
                        neighborhood.append([one-1, two])
                        inp[one-1][two] = 0
                    if one != n-1 and inp[one+1][two] == 1: # down
                        neighborhood.append([one + 1, two])
                        inp[one + 1][two] = 0
                    if two != 0 and inp[one][two - 1] == 1: # left
                        neighborhood.append([one, two - 1])
                        inp[one][two - 1] = 0
                    if two != m-1 and inp[one][two + 1] == 1: # right
                        neighborhood.append([one, two + 1])
                        inp[one][two + 1] = 0
                result[c] += 1
print(*result)



