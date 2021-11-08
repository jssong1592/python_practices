from math import ceil

m,n = map(int,input().split())

che = [True for _ in range(n-m+1)]

for i in range(2,int(n**0.5)+1):
    for j in range((ceil(m//(i**2)))*(i**2),n+1,i**2):
        if j-m < 0: continue
        che[j-m] = False

print(sum(che))