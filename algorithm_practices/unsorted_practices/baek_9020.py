che = [0,0] + [1 for i in range(10001)]
for i in range(2,10001):
    for j in range(i*2,10001,i):
        che[j] = 0
N = int(input())
for i in range(N):
    p = int(input())
    q = p // 2
    for j in range(q,1,-1):
        if che[j] == 1 and che[p-j] == 1:
            print(j, p-j)
            break