import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())
lab = []
for _ in range(n):
    lab.append(input().split())

start = []
candidate = []
space = -3

for i in range(n):
    for j in range(m):
        if lab[i][j] == '2':
            start.append((i,j))
        elif lab[i][j] == '0':
            space += 1
            candidate.append((i,j))

combi = list(combinations(candidate,3))

def bfs(i,j,lab,space):
    global ans
    dq = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    dq.append((i,j))
    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == '0':
                lab[nx][ny] = '2'
                space -= 1
                if space <= ans:
                    break
                dq.append((nx,ny))
    return space

def spread(start,lab,space):
    temp_lab = deepcopy(lab)
    for i,j in start:
        space = bfs(i,j,temp_lab,space)

    return space

ans = 0
for c in combi:
    temp_lab = deepcopy(lab)
    for i in range(3):
        x,y = c[i]
        temp_lab[x][y] = '1'
    total = spread(start,temp_lab,space)
    if total >= ans:
        ans = total

print(ans)

# def spread(combi, start,lab):
#     ans = 0
#     for each in range(len(combi)):
#         result = 0
#         for k in range(3):
#             x,y = combi[each][k]
#             lab[x][y] = '1'
#         for i,j in start:
#             bfs(i,j,lab)
#         for s in range(n):
#             for t in range(m):
#                 if lab[s][t] == '0':
#                     result += 1
#         if result >= ans:
#             ans = result
#     return ans

# print(spread(combi,start,lab))