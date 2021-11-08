'''
input
5 5
1 3
1 4
4 5
4 3
3 2
'''

import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])



result = INF
kevin = 0

for i in range(1,n+1):
    if result > sum(graph[i][1:]):
        result = sum(graph[i][1:])
        kevin = i

print(kevin)
    