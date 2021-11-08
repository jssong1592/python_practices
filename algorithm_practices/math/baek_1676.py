## 팩토리얼의 0의 개수

n = int(input())

num_lst = [[0,0] for _ in range(501)]

def two_five(num):
    result = [0,0]
    while num % 2 == 0:
        result[0] += 1
        num //= 2
    while num % 5 == 0:
        result[1] += 1
        num //= 5
    return result

for i in range(1,501):
    num_lst[i] = two_five(i)

ans = [0,0]
for i in range(1,n+1):
    ans[0] += num_lst[i][0]
    ans[1] += num_lst[i][1]

print(min(ans))