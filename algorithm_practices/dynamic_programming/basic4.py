'''
input
2 15
2
3
'''
'''
-1 input
3 4
3
5
7
'''
n,m = map(int,input().split())

coin = []

for i in range(n):
    coin.append(int(input()))

INF = int(1e9)
d = [INF] * 10001

for j in coin:
    d[j] = 1

for a in range(m+1):
    for b in coin:
        if a-b >= 0:
            d[a] = min(d[a],d[a-b]+1)

print(d[:m+1])

if d[m] < INF:
    print(d[m])
else:
    print(-1)