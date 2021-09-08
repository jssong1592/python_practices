'''
input
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

n,m = map(int,input().split())
data = []
for i in range(m):
    cmd, a, b = map(int,input().split())
    data.append((cmd,a,b))

student = list(range(n+1))
team = list(range(n+1))

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


for cmd,a,b in data:
    if cmd == 0:
        union_parent(team, a, b)
    else:
        if find_parent(team, a) == find_parent(team, b):
            print("YES")
        else:
            print("NO")

