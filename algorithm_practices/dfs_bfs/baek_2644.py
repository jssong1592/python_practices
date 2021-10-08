'''
input -> 3
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
input -> -1
9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''

from collections import deque

n = int(input())
start, end = map(int,input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
chon = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()

visited[start] = True
dq.append(start)
while dq:
    node = dq.popleft()
    for dest in graph[node]:
        if not visited[dest]:
            visited[dest] = True
            chon[dest] = chon[node] + 1
            dq.append(dest)

if chon[end] > 0:
    print(chon[end])
else:
    print(-1)