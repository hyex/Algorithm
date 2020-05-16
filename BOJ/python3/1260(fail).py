from queue import Queue
from collections import defaultdict

def bfs(graph, start_node):
    visit = {}
    # visit = list()
    queue = Queue()

    queue.put(start_node)

    while queue.qsize() > 0:
        node = queue.get()
        if node not in visit:
            visit[node] = True
            # visit.append(node)
            for nextNode in graph[node]:
                queue.put(nextNode)
    return list(visit.keys())
    # return visit


def dfs(graph, start_node):
    visit = {}
    # visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            # visit.append(node)
            stack.extend(reversed(graph[node]))
    return list(visit.keys())
    # return visit


n, m, v = map(int, input().split())
inp = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    inp[a].append(b)
    inp[b].append(a)

for key, value in inp.items():
    inp[key] = sorted(value)

d = dfs(inp, v)
b = bfs(inp, v)

for i in range(len(d)):
    print(d[i], end=" ")
print("")

for i in range(len(b)):
    print(b[i], end=" ")
print("")


