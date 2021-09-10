n = int(input())

o = [0,0,1,1] + [0] * (n-3)

for i in range(4,n+1):
    o[i] = o[i-1] + 1
    if i % 3 == 0:
        o[i] = min(o[i], o[i//3] + 1)
    if i % 2 == 0: 
        o[i] = min(o[i], o[i//2] + 1)

print(o[n])

