n, m = map(int,input().split(' '))
t = []
for i in range(n):
    t.append(list(map(int,input())))

def dfs(a, b):
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return False
    if t[a][b] == 0:
        t[a][b] = 1
        dfs(a - 1, b)
        dfs(a + 1 ,b)
        dfs(a, b - 1)
        dfs(a, b + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)