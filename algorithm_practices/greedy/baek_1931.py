'''
input -> 4
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''


n = int(input())
lst = []
for i in range(n):
    a, b = map(int,input().split())
    lst.append((a,b))

lst.sort(key=lambda x: (x[1],x[0]))


current = 0
result = 0
for i in range(len(lst)):
    if lst[i][0] >= current:
        result += 1
        current = lst[i][1]

print(result)


