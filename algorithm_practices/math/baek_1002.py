'''
input
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
output
2
1
0
'''


n = int(input())

for _ in range(n):
    a,b,c,d,e,f = map(int,input().split())
    distance = (a-d)**2 + (b-e)**2
    if distance == 0:
        if (c-f) == 0:
            print(-1)
        else:
            print(0)
    else:
        if distance == (c+f)**2 or distance == (c-f)**2:
            print(1)
        elif distance > (c+f)**2 or distance < (c-f)**2:
            print(0)
        elif distance < (c+f)**2 or distance > (c-f)**2:
            print(2)
