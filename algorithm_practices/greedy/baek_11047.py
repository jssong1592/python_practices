'''
input -> 6
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''

n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
for i in range(n-1,-1,-1):
    result += k // coins[i]
    k = k % coins[i]

print(result)