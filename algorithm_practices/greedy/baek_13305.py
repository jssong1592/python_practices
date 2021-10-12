'''
input -> 18
4
2 3 1
5 2 4 1
'''
'''
input -> 10
4
3 3 4
1 1 1 1
'''

import sys

n = int(input())
dist = list(map(int,sys.stdin.readline().rstrip().split()))
price = list(map(int,sys.stdin.readline().rstrip().split()))

current_price = price[0]
total_cost = dist[0] * current_price

for i in range(1,n-1):
    if price[i] < current_price:
        current_price = price[i]
    total_cost += dist[i] * current_price

print(total_cost)