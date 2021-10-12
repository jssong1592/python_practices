'''
input -> 32
5
3 1 4 3 2
'''

import sys

n = int(input())
person = list(map(int,sys.stdin.readline().rstrip().split()))

person.sort()

result = 0

for i in range(n):
    result += sum(person[:i+1])

print(result)
