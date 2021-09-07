'''
input
4 6
19 15 10 17
'''

import sys
import time

input = sys.stdin.readline

n,m = map(int,input().split())
cake = list(map(int,input().split()))

start_time = time.time()

def bin_search(cake, lower, upper):
    middle = (lower + upper) // 2
    cut = list(map(lambda x: x - middle if x - middle > 0 else 0, cake))
    if sum(cut) == m:
        return middle
    elif sum(cut) > m:
        return bin_search(cake, middle, upper)
    else:
        return bin_search(cake, lower, middle)

end_time = time.time()

print("time :", end_time-start_time)
print(bin_search(cake, 0, max(cake)))


