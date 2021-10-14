import sys
import heapq
from collections import Counter

lst = []
counter = Counter()

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if not lst:
            print(0)
        else:
            num = heapq.heappop(lst)
            if counter[num] > 0:
                print(-num)
                counter[num] -= 1
            else:
                print(num)
    else:
        heapq.heappush(lst, abs(a))
        if a < 0:
            counter[abs(a)] += 1