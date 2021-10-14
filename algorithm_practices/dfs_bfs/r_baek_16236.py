'''
아기상어
input -> 14
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
input -> 39
6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
input -> 48
6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
'''
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_row = i
            start_col = j
            break

def bfs(i,j, size, move, eat_count):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    dq = deque()
    next_dq = deque()
    depth = 0
    candidate = []
    graph[i][j] = 0
    dq.append((i,j))
    while dq:
        x,y = dq.popleft()
        if 0 < graph[x][y] < size:
            candidate.append((depth,x,y))
            # graph[x][y] = 0
            # eat_count -= 1
            # return [x,y, move[x][y], eat_count]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > size:
                continue
            if move[nx][ny] > 0:
                continue
            move[nx][ny] = move[x][y] + 1 
            next_dq.append((nx,ny))
        if len(dq) == 0:
            dq = next_dq
            next_dq = deque()
            depth += 1
    if len(candidate) > 0:
        candidate.sort(key=lambda x: (x[0],x[1],x[2]))
        # print(candidate)
        next_x = candidate[0][1]
        next_y = candidate[0][2]
        graph[next_x][next_y] = 0
        eat_count -= 1
        return [next_x,next_y, move[next_x][next_y], eat_count]
    return [None,None,None,None]
    

size = eat = 2
total_time = 0

while True:
    move = [[0]* n for _ in range(n)]
    # print(start_row,start_col)
    x,y, time, eat_count = bfs(start_row,start_col,size,move,eat)
    # print(graph)
    # print(time)
    if x == None:
        break
    total_time += time
    # print(total_time)
    start_row, start_col = x,y
    if eat_count == 0:
        size += 1
        eat = size
    else:
        eat = eat_count

print(total_time)