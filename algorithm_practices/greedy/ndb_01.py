'''
input => 2
5
2 3 1 2 2
'''
'''
input => 4
7
2 2 1 1 2 3 3
'''

n = int(input())

people = list(map(int,input().split()))

people.sort()

result = 0
count = 0

for person in people:
    count += 1
    if count >= person:
        result += 1
        count = 0

print(result)