'''
input -> 7
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
'''

import sys
import heapq

input = sys.stdin.readline

n,e = map(int,input().split())

INF = int(1e9)
graph = [[] for i in range(n+1)]


for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF for i in range(n+1)]
    hq = []
    distance[start] = 0
    heapq.heappush(hq,(distance[start],start))
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq,(cost,i[0]))
    return distance


distance_1 = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

result = min(distance_1[v1]+distance_v1[v2]+distance_v2[n],distance_1[v2]+distance_v1[v2]+distance_v1[n])

if result >= INF:
    print(-1)
else:
    print(result)




