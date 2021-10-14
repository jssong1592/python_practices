'''
input
3
0 3
1 5
45 50
output
3
3
4
'''

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x, y = map(int,sys.stdin.readline().rstrip().split())
    distance = y - x
    base = int(distance**0.5)
    if distance**0.5 == base:
        print(2*base - 1)
    else:
        if distance <= base**2 + base:
            print(2*base)
        else:
            print(2*base+1)
