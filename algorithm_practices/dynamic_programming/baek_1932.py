'''
input -> 30
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''

import sys

input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
    for j in range(len(tri[i])):
        tri[i][j] = max(tri[i][j] + tri[i+1][j], tri[i][j] + tri[i+1][j+1])

print(tri[0])