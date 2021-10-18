'''
input
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
output
EMPTY
333 -45
'''

import sys
import heapq

input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    min_pq = []
    max_pq = []
    visited = [False] * 1000001
    k = int(input().rstrip())
    for i in range(k):
        cmd, num = input().rstrip().split()
        if cmd == 'I':
            heapq.heappush(min_pq,(int(num),i))
            heapq.heappush(max_pq,(-int(num),i))
            visited[i] = True
        elif num == '-1':
            while min_pq and not visited[min_pq[0][1]]:
                heapq.heappop(min_pq)
            if min_pq:
                visited[min_pq[0][1]] = False
                heapq.heappop(min_pq)
        else:
            while max_pq and not visited[max_pq[0][1]]:
                heapq.heappop(max_pq)
            if max_pq:
                visited[max_pq[0][1]] = False
                heapq.heappop(max_pq)
   
    while min_pq and not visited[min_pq[0][1]]:
        heapq.heappop(min_pq)
    while max_pq and not visited[max_pq[0][1]]:
        heapq.heappop(max_pq)

    if len(min_pq) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_pq)[0],heapq.heappop(min_pq)[0])

                