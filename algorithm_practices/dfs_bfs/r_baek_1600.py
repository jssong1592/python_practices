'''
input -> 4
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0

input -> -1
2
5 2
0 0 1 1 0
0 0 1 1 0
'''
from collections import deque

k = int(input())
w,h = map(int,input().split())
Map = []
for _ in range(h):
    Map.append(list(map(int,input().split())))

visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]

def bfs():
    dq = deque()
    monkey_dx = [1,-1,0,0]
    monkey_dy = [0,0,1,-1]
    horse_dx = [2,2,1,1,-1,-1,-2,-2]
    horse_dy = [1,-1,2,-2,2,-2,1,-1]
    dq.append((0,0,k))
    visited[0][0][k] = 0
    while dq:
        x,y,z = dq.popleft()
        if x == h-1 and y == w-1:
            return visited[x][y][z]
        for i in range(4):
            monkey_nx = x + monkey_dx[i]
            monkey_ny = y + monkey_dy[i]
            if 0 <= monkey_nx < h and 0 <= monkey_ny < w and visited[monkey_nx][monkey_ny][z] == 0:
                dq.append((monkey_nx,monkey_ny,z))
                visited[monkey_nx][monkey_ny][z] = visited[x][y][z] + 1
   
        if z > 0:
            for i in range(8):
                horse_nx = x + horse_dx[i]
                horse_ny = y + horse_dy[i]
                if 0 <= horse_nx < h and 0 <= horse_ny < w and visited[horse_nx][horse_ny][z] == 0:
                    dq.append((horse_nx,horse_ny,z-1))
                    visited[horse_nx][horse_ny][z-1] = visited[x][y][z] + 1
        
    return -1

print(bfs())


