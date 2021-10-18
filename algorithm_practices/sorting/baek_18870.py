'''
input
5
2 4 -10 4 -9
output
2 3 0 3 1
'''
'''
input
6
1000 999 1000 999 1000 999
output
1 0 1 0 1 0
'''

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().rstrip().split()))
lst_set = sorted(list(set(lst)))

for i in range(len(lst)):
    print(bisect_left(lst_set, lst[i]),end=' ')
