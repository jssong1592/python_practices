'''
input
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

output
0
0
3
0
0
8
6
3
'''

import sys

input = sys.stdin.readline

def is_available(cmd,x,y):
    global n,m,dx,dy
    
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    if 0 <= nx < n and 0 <= ny < m:
        return True
    return False


def move_position(cmd, position):
    if cmd == '1':
        return [position[1][0],[7-position[0],position[1][1]]]
    elif cmd == '2':
        return [7-position[1][0],[position[0],position[1][1]]]
    elif cmd == '3':
        return [position[1][1],[position[1][0],7-position[0]]]
    else:
        return [7-position[1][1],[position[1][0],position[0]]]

dice_num = ['0' for _ in range(7)]

n,m,x,y,k = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(input().split())

dx = {'1':0,'2':0,'3':-1,'4':1}
dy = {'1':1,'2':-1,'3':0,'4':0}

position = [6,[3,5]]

cmd_lst = input().split()

for cmd in cmd_lst:
    if is_available(cmd,x,y):
        x = x + dx[cmd]
        y = y + dy[cmd]

        position = move_position(cmd, position)
        print(dice_num[7-position[0]])

        if graph[x][y] == '0':
            graph[x][y] = dice_num[position[0]]
        else:
            dice_num[position[0]] = graph[x][y]
            graph[x][y] = '0'
        