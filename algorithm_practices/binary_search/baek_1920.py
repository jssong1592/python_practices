'''
input
5
4 1 5 2 3
5
1 3 7 9 5
output
1
1
0
0
1
'''
import sys
from bisect import bisect_left, bisect_right

n = int(input())
num_list = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
m = int(input())
search_list = list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(m):
    if bisect_right(num_list, search_list[i]) == bisect_left(num_list, search_list[i]):
        print(0)
    else:
        print(1)