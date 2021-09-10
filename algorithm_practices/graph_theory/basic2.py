'''
input
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''
from collections import deque


n = int(input())

t = [0] * (n+1)
graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        if j == 0:
            t[i] = data[j]
        else:
            if data[j] == -1:
                continue
            else:
                graph[i].append(data[j])
                indegree[i] += 1

print(t)
print(graph)
print(indegree)

dq = deque()
result = []

for i in range(1,n+1):
    if indegree[i] == 0:
        dq.append(i)
        result.append(i)


while dq:
    i = dq.popleft()
    for j in range(1,n+1):
        for edge in graph[j]:
            if edge == i:
                t[j] += t[i]
                indegree[j] -= 1
        if indegree[j] == 0 and j not in result:
            dq.append(j)
            result.append(j)

print(t)
print(graph)
print(indegree)

for i in range(1,n+1):
    print(t[i])