n = int(input())

lst = [0,1,3] + [0] * 998

for i in range(3,n+1):
    lst[i] = lst[i-1] + 2 * lst[i-2]

print(lst[n]%10007)