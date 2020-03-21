# v1 : EOFerror

while True:
    try:
        N = list(map(int,input().split()))
        print(sum(N))
    except EOFError:
        break

# v2 : sys.stdin
# sys.stdin : ctrl+Z를 입력받아야 종료

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)
