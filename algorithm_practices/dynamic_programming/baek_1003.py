'''
input
3
0
1
3
'''

t = int(input())

lst = [[1,0],[0,1]]

for i in range(2,41):
    lst.append([lst[i-1][0] + lst[i-2][0],lst[i-1][1] + lst[i-2][1]])

for i in range(t):
    n = int(input())
    print(lst[n][0], lst[n][1])