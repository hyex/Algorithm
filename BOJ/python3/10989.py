
import sys

N = int(sys.stdin.readline())
inp = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    inp[a] = inp[a] + 1


for i in range(len(inp)):
    if inp[i] != 0:
        for j in range(inp[i]):
            sys.stdout.write(str(i) + '\n')

