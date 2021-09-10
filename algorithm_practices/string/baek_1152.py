from sys import stdin

data = stdin.readline().rstrip().lstrip().split(' ')

if data == ['']:
    print(0)
else:
    print(len(data))