# try-except 문을 통한 indexError 처리

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1+(min2*2))
        except IndexError:
            return -1
        answer += 1
    return answer
