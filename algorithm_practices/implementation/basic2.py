n = int(input())

result = 0

for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in f'{i}:{j}:{k}':
                result += 1

print(result)