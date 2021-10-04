'''
input
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for j in range(1,n+1):
    graph[j][j] = 0

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)
