from collections import Counter

n = int(input())

district = []

for i in range(n):
    district.append(list(map(int,input())))

def dfs(a,b,c):
    if a < 0 or b < 0 or a >= n or b >= n:
        return False
    if district[a][b] == 1:
        district[a][b] += c
        dfs(a-1,b,c)
        dfs(a+1,b,c)
        dfs(a,b-1,c)
        dfs(a,b+1,c)
        return True
    return False

c = 1
for a in range(n):
    for b in range(n):
        if dfs(a,b,c):
            c += 1

result = Counter()

for row in district:
    for house in row:
        result[house] += 1

r = [result[key] for key in result if key != 0]
r.sort()

print(len(r))
for i in r:
    print(i)


            
