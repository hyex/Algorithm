def solution(n, computers):
    answer = 0
    end = dict()
    for idx in range(n):
        if idx not in end:
            end[idx] = True
            temp = set()
            temp.add(idx)
            while temp:
                computer = temp.pop()
                for i in range(0, n):
                    if computers[computer][i] == 1 and computer != i:
                        if i not in end:
                            temp.add(i)
                            end[i] = True
            answer += 1
    return answer
