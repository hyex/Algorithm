import sys
while True:
    # sys의 readline이 input 함수보다 속도가 
    a, b = sys.stdin.readline().split()
    a = int(a); b = int(b)
    if a + b == 0:
        break
    print(a + b)
