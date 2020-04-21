import heapq


def solution(jobs):

    jobs.sort()
    answer = 0
    now = 0
    exist = -1
    heap = []
    result = []

    while jobs:
        for idx in range(len(jobs)):
            start, time = jobs[idx]
            if start < now:
                heapq.heappush(heap, [time, start])
            else:
                if not heap:
                    exist = idx
                break
        if exist == -1:
            time, start = heapq.heappop(heap)
            heap = []
            now += time
            result.append(now - start)
            jobs.remove([start, time])
        else:
            start, time = jobs[exist]
            now = start + time
            result.append(now - start)
            jobs.remove([start, time])
            exist = -1

    answer = sum(result) // len(result)
    return answer
