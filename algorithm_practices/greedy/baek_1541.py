'''
input -> -35
55-50+40
'''

import sys
import re

calc = sys.stdin.readline().rstrip()
nums = list(map(int,re.split('[+-]',calc)))
exp = re.split('[0-9]',calc)
exp = [x for x in exp if x]

minus = 0
for i in range(len(exp)):
    if exp[i] == '-':
        minus |= 1
    else:
        if minus == 1:
            exp[i] = '-'

result = nums[0]

for i in range(len(nums)-1):
    if exp[i] == '-':
        result -= nums[i+1]
    else:
        result += nums[i+1]

print(result)