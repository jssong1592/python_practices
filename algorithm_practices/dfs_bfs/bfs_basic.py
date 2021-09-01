'''
큐 개념, collections deque 쓰기
'''
from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)

def bfs(graph, v, visited):
    visited[v] = True
    dq = deque([v])
    while dq:
        p = dq.popleft()
        print(p)
        for i in graph[p]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True

bfs(graph, 1, visited)
