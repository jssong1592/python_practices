'''
input
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
from sys import stdin

input = stdin.readline

n = int(input())

graph = [[] for i in range(n+1)] 
parent = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, parent):
    stack = [start]
    
    while stack:
        node = stack.pop()
        for i in graph[node]:
            parent[i].append(node)
            stack.append(i)
            graph[i].remove(node)
    return parent

for i in dfs(graph,1,parent)[2:]:
    print(i[0])
