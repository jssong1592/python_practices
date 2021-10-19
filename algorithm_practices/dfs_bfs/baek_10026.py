'''
input
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
output
4 3
'''
from collections import deque
n = int(input())

graph = []
for i in range(n):
    graph.append(input())

visited = [[[False,False] for j in range(n)] for i in range(n)]

def bfs(i,j,graph,blind):
    dq = deque()
    dq.append((i,j))
    visited[i][j][blind] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while dq:
        x,y = dq.popleft()
        color = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if visited[nx][ny][blind]:
                continue
            if blind == 1:
                if (color in ['R','G'] and graph[nx][ny] == 'B') or (color == 'B' and graph[nx][ny] in ['R','G']):
                    continue
            elif blind == 0:
                if graph[nx][ny] != color:
                    continue
            dq.append((nx,ny))
            visited[nx][ny][blind] = True
            
    return 1

num = [0,0]

for i in range(n):
    for j in range(n):
        for k in range(2):
            if not visited[i][j][k]:
                num[k] += bfs(i,j,graph,k)

print(num[0], num[1])

            

        


