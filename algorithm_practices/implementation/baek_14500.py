'''
input -> 19
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

input -> 20
4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

input -> 7
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
result = []
ans = 0
def dfs(x,y,candidate,cnt,total):
    global ans
    candidate.append((x,y))
    visited[x][y] = True

    if len(candidate) == 4:
        if ans < total:
            ans = total
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for c in candidate:
        x = c[0]
        y = c[1]
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and cnt < 4:
                visited[nx][ny] = True
                dfs(nx,ny,candidate, cnt + 1,total + graph[nx][ny])
                visited[nx][ny] = False
                candidate.pop()
            
for i in range(n):
    for j in range(m):
        dfs(i,j,[],1,graph[i][j])
        
print(ans)
