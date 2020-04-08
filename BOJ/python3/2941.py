# 원래 사용할라했던 string.lstrip(문자) 함수는 문자열 왼쪽 제거 함수지만,
# 문자 지정이 없으면 공백문자를 제거. 지정되어 있으면 chars의 모든 조합을 제거한다는 것을 명심

word = input()
prefix = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
result = 0
isExist = False


while word != "":
    for p in prefix:
        if word.startswith(p):
            result += 1
            cutLength = len(p)
            word = word[cutLength:]
            isExist = True
            break
    if isExist is False:
        result += 1
        word = word[1:]
    else:
        isExist = False

print(result)
