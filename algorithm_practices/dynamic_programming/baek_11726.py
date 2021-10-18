'''
input -> 2
2
input -> 55
9
'''
'''
n == 1
1
n == 2
1 + f(1) => 2
n == 3
f(2) + f(1) => 3
n == 4
f(3) + f(2)
'''
n = int(input())

lst = [0,1,2] + [0] * 998
for i in range(3,1001):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n]%10007)