'''
input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''
from collections import deque

v,e = map(int,input().split())

edges = [[] for i in range(v+1)]
indegrees = [0] * (v+1)

for i in range(e):
    a, b = map(int,input().split())
    edges[a].append(b)
    indegrees[b] += 1
     

print(indegrees)

dq = deque()

result = []

for i in range(1,v+1):
    if indegrees[i] == 0:
        dq.append(i)

while dq:
    node = dq.popleft()
    result.append(node)
    for n in edges[node]:
        indegrees[n] -= 1
        if indegrees[n] == 0:
            dq.append(n)

print(result)
