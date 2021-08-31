import sys

N = 123456 * 2

che = [0,0] + [1] * (N-1)
for i in range(2,int(N**0.5)+1):
    j = 2
    while i * j <= N:
        che[i*j] = 0
        j += 1

for num in sys.stdin:
    if int(num) == 0:
        continue
    print(sum(che[int(num)+1:int(num)*2 + 1]))