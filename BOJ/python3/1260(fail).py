from queue import Queue
from collections import defaultdict


def dfs(graph, start_node):
    visited = [0 for _ in range(n+1)]
    stack = list()
    result = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            result.append(node)
            stack.extend(x for x in reversed(graph[node]) if x not in result)

    return result


def bfs(graph, start_node):
    visited = [0 for _ in range(n + 1)]
    result = []
    # visit = {}
    # visit = list()
    queue = Queue()

    queue.put(start_node)

    while queue.qsize() > 0:
        node = queue.get()
        if visited[node] == 0:
            visited[node] = 1
            result.append(node)
            for nextNode in graph[node]:
                if nextNode not in result:
                    queue.put(nextNode)
    return result


n, m, v = map(int, input().split())
inp = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    inp[a].append(b)
    inp[b].append(a)

for key, value in inp.items():
    inp[key] = sorted(value)

print(*dfs(inp, v))
print(*bfs(inp, v))



# 1260 에서 먹힌 코드
# 내 코드(위)가 안되는 이유는 아직도 모르겠다

# def dfs(v):
#     print(v, end=' ')
#     visit[v] = 1
#     for i in range(1, n+1):
#         if visit[i] == 0 and s[v][i] == 1:
#             dfs(i)

# def bfs(v):
#     queue = [v]
#     visit[v] = 0
#     while(queue):
#         v = queue[0]
#         print(v, end=' ')
#         del queue[0]
#         for i in range(1, n+1):
#             if visit[i] == 1 and s[v][i] == 1:
#                 queue.append(i)
#                 visit[i] = 0

# n, m, v = map(int, input().split())
# s = [[0] * (n + 1) for i in range(n+1)]
# visit = [0 for i in range(n + 1)]
# for i in range(m):
#     x,y = map(int, input().split())
#     s[x][y] = 1
#     s[y][x] = 1

# dfs(v)
# print()
# bfs(v)
