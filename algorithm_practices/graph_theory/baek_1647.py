import sys

input = sys.stdin.readline

n,m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

parent = list(range(n+1))    
    
edges = []

for i in range(m):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

result = []

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))