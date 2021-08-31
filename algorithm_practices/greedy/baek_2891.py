n, s, r = map(int, input().split(' '))
broken = set(map(int, input().split(' ')))
reserve = set(map(int, input().split(' ')))

result = 0
inter = broken & reserve

broken -= inter
reserve -= inter

broken = list(broken)
reserve = list(reserve)

for i in broken:     
    if i-1 in reserve:
        reserve.remove(i-1)
    elif i+1 in reserve:
        reserve.remove(i+1)
    else:
        result += 1
print(result)