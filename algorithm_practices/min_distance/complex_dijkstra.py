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


# use heapq
import heapq

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    hq = []
    distance[start] = 0
    heapq.heappush(hq,(distance[start], start))
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq,(cost, i[0]))

dijkstra(start)

print(distance)