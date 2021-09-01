'''
스택 개념, 재귀함수 추천, 부득이할 땐 스택 라이브러리 쓰기
'''

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

def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)