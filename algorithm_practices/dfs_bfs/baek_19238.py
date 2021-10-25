'''
input -> 14
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''
'''
input -> -1
6 3 13
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5

6 3 100
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''
import sys
import heapq
from collections import deque

input = sys.stdin.readline


INF = int(1e9)
n, m, fuel = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

a,b =  map(int,input().split())
start = [a-1,b-1]

guests = []
destinations = {}

for _ in range(m):
    a,b,c,d = map(int,input().split())
    guests.append([a-1,b-1])
    destinations[(a-1,b-1)] = [c-1,d-1] 

def is_available(i,j):
    global graph, n
    if 0 <= i < n and 0 <= j < n and graph[i][j] == 0:
        return True
    return False

def bfs(i,j):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[INF for _ in range(n)] for _ in range(n)]
    dq = deque()
    dq.append((i,j))
    distance[i][j] = 0
    visited[i][j] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_available(nx,ny) and not visited[nx][ny]:
                dq.append((nx,ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
    return distance

def pickup_guest(i,j):
    global guests, destinations
    distance = bfs(i,j)
    candidate = []
    for guest in guests:
        heapq.heappush(candidate,(distance[guest[0]][guest[1]],guest[0],guest[1]))
    
    if len(candidate) > 0:
        dist, guest_x, guest_y = heapq.heappop(candidate)
        destination = destinations[(guest_x,guest_y)]
        guests.remove([guest_x,guest_y])
        return (dist, [guest_x,guest_y], destination)
    return (-1,-1,-1)

def to_destination(guest, destination):
    distance = bfs(guest[0],guest[1])
    
    dist = distance[destination[0]][destination[1]]
    
    return dist

cnt = len(guests)
ok = True

while cnt > 0:
    dist, guest, destination = pickup_guest(start[0],start[1])
    
    if dist == INF or dist > fuel:
        ok = False
        break
    fuel -= dist
    
    dist = to_destination(guest, destination)
    if dist == INF or fuel - dist < 0:
        ok = False
        break
    fuel = fuel - dist + 2*dist
    
    cnt -= 1
    start = destination

if not ok:
    print(-1)
else:
    print(fuel)




