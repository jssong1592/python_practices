'''
input
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
output
YES
NO
'''
import sys
from collections import deque

def bfs(v,graph,color):
    for i in range(1,v+1):
        if color[i] != 0:
            continue
        dq = deque()
        color[i] = 1
        dq.append((i,color[i]))
        while dq:
            node, c = dq.popleft()
            for dest in graph[node]:
                if color[dest] == 0:
                    if c == 1:
                        color[dest] = 2
                    elif c == 2:
                        color[dest] = 1
                    dq.append((dest,color[dest]))
                elif color[dest] == c:
                    return "NO"
    return "YES"

k = int(input())
result = []
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for i in range(v+1)]
    color = [0 for i in range(v+1)]
    for _ in range(e):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    result.append(bfs(v,graph,color))
    

for i in range(k):
    print(result[i])
