'''
input
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

'''
import sys
sys.setrecursionlimit(10**5)


t = int(input())
for i in range(t):
    count = 0
    m, n, k = map(int,input().split())
    farm = [[0] * m for j in range(n)]
    for a in range(k):
        x, y = map(int,input().split())
        farm[y][x] = 1
    
    def dfs(x,y):
        if x <= -1 or y <= -1 or x >= m or y >= n:
            return False
        if farm[y][x] == 1:
            farm[y][x] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False

    for p in range(m):
        for q in range(n):
            if dfs(p,q):
                count += 1
    print(count)