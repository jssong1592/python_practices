from collections import deque
import sys

input = sys.stdin.readline

haveto = 0
tmt = deque()
res = 0

x,y,z = map(int,input().split())

graph = [[] for i in range(z)]
for i in range(z):
    for j in range(y):
        graph[i].append(input().split())
        for k in range(x):
            if graph[i][j][k] == '0':
                haveto += 1
            elif graph[i][j][k] == '1':
                tmt.append((i,j,k))

# print(graph)
# print(haveto)
# print(tmt)

while tmt and haveto:
    l = len(tmt)
    for _ in range(l):
        i,j,k = tmt.popleft()
        if i + 1 < z and graph[i+1][j][k] == '0':
            tmt.append((i+1,j,k))
            graph[i+1][j][k] = 1
            haveto -= 1
        if i > 0 and graph[i-1][j][k] == '0':
            tmt.append((i-1,j,k))
            graph[i-1][j][k] = 1
            haveto -= 1
        if j + 1 < y and graph[i][j+1][k] == '0':
            tmt.append((i,j+1,k))
            graph[i][j+1][k] = 1
            haveto -= 1
        if j > 0 and graph[i][j-1][k] == '0':
            tmt.append((i,j-1,k))
            graph[i][j-1][k] = 1
            haveto -= 1
        if k + 1 < x and graph[i][j][k+1] == '0':
            tmt.append((i,j,k+1))
            graph[i][j][k+1] = 1
            haveto -= 1
        if k > 0 and graph[i][j][k-1] == '0':
            tmt.append((i,j,k-1))
            graph[i][j][k-1] = 1
            haveto -= 1
    res += 1

if haveto > 0:
    print(-1)
else:
    print(res)


