'''
input
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
output
5
28
0
'''


from collections import deque

def bfs(n,a,b,da,db):
    graph = [[0 for i in range(n)] for j in range(n)]
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [-2,2,-1,1,-2,2,-1,1]
    dq = deque()
    graph[a][b] = 0
    dq.append((a,b))
    while dq:
        # print(dq)
        x, y = dq.popleft()
        if x == da and y == db:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx,ny))
                

cases = int(input())

for case in range(cases):
    n = int(input())
    a,b = map(int,input().split())
    da,db = map(int,input().split())
    print(bfs(n,a,b,da,db))