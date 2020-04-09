# 문제점
# 라이브러리 사용과 문법 숙지가 

# 다른 사람 풀이

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
    
# 내 풀이

def solution(clothes):
    answer = 1

    kinds = set()
    for cloth in clothes:
        kinds.add(cloth[1])
    kinds = list(kinds)

    count = list(0 for _ in range(len(kinds)))

    for index in range(len(kinds)):
        for cloth in clothes:
            if cloth[1] == kinds[index]:
                count[index] += 1

    for i in count:
        answer = answer * (i+1)

    return answer - 1
