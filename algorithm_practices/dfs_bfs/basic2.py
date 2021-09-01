'''
input
5 6
101010
111111
000001
111111
111111
'''
'''
output
10
'''

from collections import deque

n, m = map(int, input().split(' '))
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()

        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na in range(n) and nb in range(m) and maze[na][nb] == 1:
                q.append((na,nb))
                maze[na][nb] = maze[a][b] + 1
    return maze[n-1][m-1]

print(bfs(0,0))



# def dfs(a, b, count):
#     if a == n - 1 and b == m - 1:
#         return count
    
#     if a <= -1 or a >= n or b <= -1 or b >= m or maze[a][b]==0:
#         return 0
    
#     maze[a][b] = 0
#     count += 1
#     result = dfs(a-1,b,count) + dfs(a+1,b,count) + dfs(a,b-1,count) + dfs(a,b+1,count)

#     return result

# print(dfs(0,0,1))