# 엄청 어렵게 풀고 있었는데, 너무 쉬운 풀이
# https://leedakyeong.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-1316%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4-in-python

cnt = 0
for i in range(int(input())):
    word = input()
    cnt+=list(word) == sorted(word, key=word.find)
print(cnt)
