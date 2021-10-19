'''
input
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
output
[2,1]
error
[1,2,3,5,8]
error
'''


import sys
from collections import Counter

input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    lst = input()
    if n > 0:
        lst = lst[1:-2].split(',')
    else:
        lst = []
    c = Counter(p)
    if c['D'] > len(lst):
        print("error")
        continue
    elif c['D'] == len(lst):
        lst = []
        print(lst)
        continue
    else:
        reverse = 0
        for ch in p:
            if ch == 'R':
                reverse ^= 1
            else:
                if reverse == 0:
                    lst.pop(0)
                else:
                    lst.pop()
        if reverse == 1:
            lst = lst[::-1]
        print('['+','.join(lst)+']')
    