'''
input
9
5 12 7 10 9 1 2 3 11
13
output
3
'''

import sys

n = int(input())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
x = int(input())

count = 0

nums.sort()
# 1 2 3 5 7 9 10 11 12
i = 0
j = len(nums) - 1
while i < j:
    if nums[i] + nums[j] > x:
        j -= 1
    elif nums[i] + nums[j] < x:
        i += 1
    elif nums[i] + nums[j] == x:
        count += 1
        i += 1
        j -= 1

print(count)