'''
input
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''

n, m = map(int,input().split())

d = []
for j in range(m):
    a,b,c = map(int,input().split())
    d.append((c,a,b))

parent = list(range(n+1))

def find_parent(parent, x):
    if parent[x] != x:
       parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

d.sort()

cost = 0

for e in d:
    if find_parent(parent, e[1]) != find_parent(parent, e[2]):
        union_parent(parent, e[1], e[2])
        cost += e[0]

print(cost)