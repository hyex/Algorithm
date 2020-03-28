"""
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
"""

# 다시보기

n = int(input())
x = n
for i in range(1, n+1):
    print(' '*(i-1) + '*'*(2*(x-i)+1))
for k in range(1, x):
    print(' '*(x-k-1) + '*'*(2*k+1))
