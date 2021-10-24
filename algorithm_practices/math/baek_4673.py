num_lst = [True] * 10001

def digit_total(num):
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result

for i in range(1,10001):
    d_i = i + digit_total(i)
    while d_i < 10001 and num_lst[d_i]:
        num_lst[d_i] = False
        d_i = d_i + digit_total(d_i)

for i in range(1,10001):
    if num_lst[i]:
        print(i)

