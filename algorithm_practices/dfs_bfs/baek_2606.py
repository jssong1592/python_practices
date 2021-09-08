n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]


for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

virus = [False] * (n+1)

def dfs(v):
    virus[v] = True
    for node in graph[v]:
        if not virus[node]:
            dfs(node)

dfs(1)
if True in virus:
    print(virus.count(True)-1)
else:
    print(0)


# def find_parent(parent, x):
#     if parent[x] != x:
#         parent = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

# parent = list(range(n+1))