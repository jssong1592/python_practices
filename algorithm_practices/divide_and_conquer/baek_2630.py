'''
input
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
output
9
7
'''

import sys

white_blue = [0,0]

def func(paper):
    if sum([sum(x) for x in paper]) == len(paper)**2:
        white_blue[1] += 1
    elif sum([sum(x) for x in paper]) == 0:
        white_blue[0] += 1
    else:
        first = [[paper[i][j] for j in range(len(paper)//2)] for i in range(len(paper)//2)]
        second = [[paper[i][j+len(paper)//2] for j in range(len(paper)//2)] for i in range(len(paper)//2)]
        third = [[paper[i+len(paper)//2][j] for j in range(len(paper)//2)] for i in range(len(paper)//2)]
        fourth = [[paper[i+len(paper)//2][j+len(paper)//2] for j in range(len(paper)//2)] for i in range(len(paper)//2)]
        func(first)
        func(second)
        func(third)
        func(fourth)

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().rstrip().split())))

func(paper)

print(white_blue[0])
print(white_blue[1])


