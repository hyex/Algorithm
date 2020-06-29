# 2751 (05m)

import sys

N = int(sys.stdin.readline())
inp = [0] * N
for i in range(N):
    inp[i] = int(sys.stdin.readline())

inp.sort()

for i in range(N):
    sys.stdout.write(str(inp[i]) + '\n')


