M = int(input())
N = int(input())

lst = []

for i in range(M,N+1):
    if i == 2 or i == 3:
        lst.append(i)
    elif i > 3 and i % 2 == 1:
        a = 3
        while a < i:
            if i % a != 0:
                a += 2
            else:
                break
        if a == i:
            lst.append(i)
if not lst:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])

    sorted()