'''
input
5
-2 4 -99 -1 98
'''
import sys

n = int(input())
nums = list(map(int,sys.stdin.readline().rstrip().split()))

nums.sort()
# -99 -2 -1 1 4 98

i = 0
j = n - 1
INF = 2 * int(1e9)
mix = INF
mix1 = nums[i]
mix2 = nums[j]

while i < j:
    if abs(nums[i] + nums[j]) <= mix:
        mix = abs(nums[i]+nums[j])
        mix1 = nums[i]
        mix2 = nums[j]
    if abs(nums[i+1]+nums[j]) < abs(nums[i] + nums[j]):
        i += 1
    else:
        j -= 1

print(mix1, mix2)