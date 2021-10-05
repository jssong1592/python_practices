'''
input -> 15
6 4
0100
1110
1000
0000
0111
0000
input -> -1
4 4
0111
1111
1111
1110
'''
from collections import deque


n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

visited = [[[-1] * 2 for i in range(m)] for j in range(n)]

def bfs():
    dq = deque()
    dq.append((0,0,0))
    visited[0][0][0] = 1
    while dq:
        r, c, z = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < m:
            
                if graph[nr][nc] == 0 and visited[nr][nc][z] == -1:
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    dq.append((nr,nc,z))
                    print(visited)
                elif z == 0 and graph[nr][nc] == 1 and visited[nr][nc][1] == -1:
                    visited[nr][nc][1] = visited[r][c][z] + 1
                    dq.append((nr,nc,1))
                    print(visited)

bfs()

ans1,ans2 = visited[n-1][m-1][0],visited[n-1][m-1][1]

if ans1 != -1 and ans2 == -1:
    print(ans1)
elif ans1 == -1 and ans2 != -1:
    print(ans2)
else:
    print(min(ans1,ans2))



    