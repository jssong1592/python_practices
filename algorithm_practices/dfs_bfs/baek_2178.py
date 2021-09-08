from collections import deque

n,m = map(int,input().split())

maze = []

for i in range(n):
    maze.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    dq = deque()
    dq.append((a,b))
    while dq:
        a,b = dq.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na < 0 or na >= n or nb < 0 or nb >= m:
                continue
            if maze[na][nb] == 1:
                dq.append((na,nb))
                maze[na][nb] = maze[a][b] + 1
                
bfs(0,0)

print(maze[n-1][m-1])