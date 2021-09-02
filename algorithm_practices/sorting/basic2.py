n = int(input())
arr = []
for i in range(n):
    arr.append(input().split(' '))
    arr[i][1] = int(arr[i][1])

arr.sort(key=lambda x:x[1])

for i in arr:
    print(i[0], end= ' ')