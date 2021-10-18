'''
input -> 2
6 5
1 2
2 5
5 1
3 4
4 6
'''
'''
input -> 1
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''

import sys
from collections import deque

v, e = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for i in range(v+1)]
visited = [False] * (v+1)
count = 0

for _ in range(e):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()
for i in range(1,v+1):
    if not visited[i]:
        count += 1
        visited[i] = True
        dq.append(i)
        while dq:
            node = dq.popleft()
            for dest in graph[node]:
                if not visited[dest]:
                    visited[dest] = True
                    dq.append(dest)

print(count)