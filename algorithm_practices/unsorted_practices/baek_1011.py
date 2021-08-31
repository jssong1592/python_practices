def countDist(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    k = 1
    while k**2 <= n:
        k+=1
    return countDist(n-(k-1)**2) + 2*(k-1)-1

T = int(input())
a = [list(map(int,input().split())) for i in range(T)]
print(a)
for each in a:
    dist = each[1] - each[0]
    print(countDist(dist))
       
    