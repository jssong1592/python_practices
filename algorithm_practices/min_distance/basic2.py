'''
input
3 2 1
1 2 4
1 3 2
'''

import sys
import heapq

input =sys.stdin.readline

n,m,c = map(int, input().split())

INF = int(1e9)

distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    q,w,e = map(int, input().split())
    graph[q].append((w,e))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(hq,(cost, i[0]))

dijkstra(c)

result = [distance[i] for i in range(1,n+1) if distance[i] < INF and distance[i] > 0]

print(distance)
print(result)
print(len(result), max(result))
