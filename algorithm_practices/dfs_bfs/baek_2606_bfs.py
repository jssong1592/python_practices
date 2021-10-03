from collections import deque

n = int(input())
e = int(input())

graph = [[] for i in range(n+1)]
virus = [False for i in range(n+1)]

for i in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()
dq.append(1)
virus[1] = True
while dq:
    node = dq.popleft()
    virus[node] = True
    for i in graph[node]:
        if not virus[i]:
            dq.append(i)

print(sum(virus)-1)