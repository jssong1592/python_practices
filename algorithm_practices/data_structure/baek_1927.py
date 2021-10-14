'''
input
9
0
12345678
1
2
0
0
0
0
32
'''
'''
output
0
1
2
12345678
0
'''
import sys
import heapq

lst = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if not lst:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, a)