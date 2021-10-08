from collections import deque

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
indegrees = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegrees[b] += 1

dq = deque()

for i in range(1,n+1):
    if indegrees[i] == 0:
        dq.append(i)

while dq:
    node = dq.popleft()
    print(node, end=' ')
    for dest in graph[node]:
        indegrees[dest] -= 1
        if indegrees[dest] == 0:
            dq.append(dest)

