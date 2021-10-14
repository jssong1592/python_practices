'''
input -> 11
2 3 1
'''
'''
input -> 63
3 7 7
'''
n, r, c = map(int,input().split())

size = n
row = r + 1
col = c + 1

quadrant = []

while size > 0:
    if row > (2**size) // 2:
        if col > (2**size) // 2:
            quadrant.append(4)
            row -= (2**size) // 2
            col -= (2**size) // 2
        else:
            quadrant.append(3)
            row -= (2**size) // 2
    else:
        if col > (2**size) // 2:
            quadrant.append(2)
            col -= (2**size) // 2
        else:
            quadrant.append(1)
    size -= 1

start = 4 ** n
for i in range(len(quadrant)):
    start -= 4**(len(quadrant)-1-i)*(4-quadrant[i])

print(start-1)
print(quadrant)

