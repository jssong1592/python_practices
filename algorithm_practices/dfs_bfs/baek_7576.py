'''
input -> -1
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

input -> 6
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

input -> 8
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

input -> 14
5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0

input -> 0
2 2
1 -1
-1 1
'''

from collections import deque

m, n = map(int,input().split())

graph = []
q1 = deque()
q2 = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

day = 0

for i in range(n):
    graph.append(list(map(int,input().split())))

# print(graph)

for x in range(m):
    for y in range(n):
        if graph[y][x] == 1:
            q1.append((x,y))

while True:
    while q1:
        x,y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q2.append((nx,ny))
    if not q2:
        break
    day += 1
    # print(day)
    # print(graph)
    q1 = q2
    q2 = deque()

total = sum([sum(graph[x]) for x in range(n)])

if total % 2 != (m*n) % 2:
    print(-1)
else:
    print(day)
