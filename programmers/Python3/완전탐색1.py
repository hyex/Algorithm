def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]
    pIdx = -1
    for p in p1, p2, p3:
        idx = 0
        pIdx += 1
        for correct in answers:
            if idx == len(p):
                idx = 0
            if correct == p[idx]:
                result[pIdx] += 1
            idx += 1
            
    maxValue = max(result)

    for i in range(len(result)):
        if result[i] == maxValue:
            answer.append(i + 1)

    answer.sort()

    return answer
