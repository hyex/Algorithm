# 11650 21:11 - 21 (10m)

import sys

N = int(sys.stdin.readline())
inp = []

for i in range(N):
    inp.append(list(map(int, sys.stdin.readline().split())))

inp.sort(key=lambda a: (a[0], a[1]))

for i in range(N):
    # print(*inp[i])
    sys.stdout.write(str(inp[i][0]) + ' ' + str(inp[i][1]) + '\n')
