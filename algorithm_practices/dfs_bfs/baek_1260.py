from collections import deque

n,m,v = map(int,input().split())

edges = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

for each in edges:
    each.sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for node in edges[v]:
        if not visited[node]:
            dfs(node)

def bfs(v):
    visited = [False] * (n+1)
    dq = deque()
    dq.append(v)
    visited[v] = True
    while dq:
        now = dq.popleft()
        print(now, end=' ')
        for node in edges[now]:
            if not visited[node]:
                dq.append(node)
                visited[node] = True


dfs(v)
print()
bfs(v)