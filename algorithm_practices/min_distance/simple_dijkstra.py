'''
input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3 
2 4 2
3 2 3
3 6 5
4 3 3 
4 5 1
5 3 1
5 6 2
'''

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if not visited[i] and distance[i]< min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for node, dist in graph[start]:
            distance[node] = dist
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for node, dist in graph[now]:
            if distance[node] > distance[now] + dist:
                distance[node] = distance[now] + dist
    

dijkstra(start)

print(distance)