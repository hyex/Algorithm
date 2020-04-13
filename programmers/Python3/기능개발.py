# 계속 testcase 2번을 틀리는 코드
# 무엇이 문제인가

def solution(progresses, speeds):
    answer = []
    progresses = progresses[::-1]
    speeds = speeds[::-1]

    while progresses:
        count = 1
        value = progresses.pop()
        days = round((100 - value) / speeds.pop())
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + days * speeds[i]

        while progresses and progresses[-1] >= 100:
            count += 1
            progresses.pop()
            speeds.pop()
        answer.append(count)

    return answer
