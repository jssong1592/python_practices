n = int(input())

INF = int(1e9)

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(1,n+1):
    lst = input().split()
    for j in range(n):
        graph[i][j+1] = lst[j]



for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] == '1' and graph[k][j] == '1':
                graph[i][j] = '1'

for i in range(1,n+1):
    print(' '.join(graph[i][1:]))
    