'''
input
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
output
0
2
3
7
INF
'''
import sys
import heapq
input = sys.stdin.readline
v,e = map(int,input().split())
start = int(input())
INF = int(1e9)
distance = [INF for i in range(v+1)]
visited = [False for i in range(v+1)]
graph = [[] for i in range(v+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,v+1):
#         if not visited[i] and distance[i] < min_value:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     visited[start] = True
#     distance[start] = 0
#     for node, dist in graph[start]:
#         distance[node] = dist
#     for i in range(v-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for node, dist in graph[now]:
#             cost = dist + distance[now]
#             if cost < distance[node]:
#                 distance[node] = cost

def dijkstra(start):
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
                heapq.heappush(hq,(distance[i[0]],i[0]))


dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
            
    