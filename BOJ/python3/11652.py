# 11652 19:00 - 23 (23m)

import sys

N =  int(sys.stdin.readline())
dic = dict()

for i in range(N):
    x = int(sys.stdin.readline())

    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

# 가장 큰 value 값을 찾는다
maximum = max(dic.values())


# 그 value 값을 가지는 key의 리스트 생성
keylist = []
for k, v in dic.items():
    if v == maximum:
        keylist.append(k)


# key 리스트에서 가장 작은 값을 출력한다.
print(min(keylist))
