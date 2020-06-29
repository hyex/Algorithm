# 11651 21:23 - 24 (01m)

import sys

N = int(sys.stdin.readline())
inp = []

for i in range(N):
    inp.append(list(map(int, sys.stdin.readline().split())))

inp.sort(key=lambda a: (a[1], a[0]))

for i in range(N):
    # print(*inp[i])
    sys.stdout.write(str(inp[i][0]) + ' ' + str(inp[i][1]) + '\n')
