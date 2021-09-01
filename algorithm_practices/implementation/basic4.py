'''
input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 
'''
'''
output
3
'''

n, m = map(int,input().split(' '))
a, b, d = map(int,input().split(' '))
world = []
for i in range(n):
    world.append(list(map(int, input().split())))

result = 1
direction = {0:(-1, 0), 1:(0,1), 2:(1,0), 3:(0,-1)}
rotate = 0

while True:
    d = (d+3)%4
    print('d =', d)
    if world[a + direction[d][0]][b + direction[d][1]] == 0:
        world[a][b] = -1
        a += direction[d][0]
        b += direction[d][1]
        result += 1
        rotate = 0
        print(f'i am now at : world{a}{b}', world[a][b])
    else:
        rotate += 1
    
    if rotate == 4:
        if world[a - direction[d][0]][b - direction[d][1]] != 1:
            world[a][b] = -1
            a -= direction[d][0]
            b -= direction[d][1]
            rotate = 0
            print(f'i am now at : world{a}{b}', world[a][b])
        else:
            break

print(result)
