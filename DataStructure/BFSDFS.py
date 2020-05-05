from queue import Queue

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


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['C', 'H'],
        'C': ['D'],
        'D': ['E', 'G'],
        'E': ['F'],
        'F': [],
        'G': [],
        'H': ['I', 'J', 'M'],
        'I': [],
        'J': ['K'],
        'K': ['L'],
        'L': ['K'],
        'M': []
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))
