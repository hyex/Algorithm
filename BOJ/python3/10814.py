# 10814 21:25 - 27 (02m)

import sys

N = int(sys.stdin.readline())
inp = []

for i in range(N):
    inp.append(list(sys.stdin.readline().split()))

inp.sort(key=lambda a: (int(a[0])))

for i in range(N):
    # print(*inp[i])
    sys.stdout.write(str(inp[i][0]) + ' ' + str(inp[i][1]) + '\n')
