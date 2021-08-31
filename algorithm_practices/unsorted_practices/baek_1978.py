n = int(input())
lst = list(map(int,input().split()))
result = 0
for i in range(n):
    if lst[i] == 2 or lst[i] == 3:
        result += 1
    else:
        if lst[i] > 3 and lst[i] % 2 == 1:
            a = 3
            result += 1
            while a < lst[i]:
                if lst[i] % a == 0:
                    result -= 1
                    break
                a += 2
print(result)