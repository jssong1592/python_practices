n = int(input())
cmd = input().split(' ')

x = y = 1

directions = ['U','D','L','R']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for each in cmd:
    if (each == 'U' and y == 1) or (each == 'D' and y == n) or (each == 'R' and x == n) or (each == 'L' and x == 1):
        continue
    x += dx[directions.index(each)]
    y += dy[directions.index(each)]

print(y, x)