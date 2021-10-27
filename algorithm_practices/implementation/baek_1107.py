destination = int(input())
n = int(input())
broken = []
if n > 0:
    broken = list(map(int,input().split()))

def has_num(dest,num_list):
    for num in num_list:
        temp = dest
        if temp == 0:
            if temp in num_list:
                return True
        while temp > 0:
            if num == temp % 10:
                return True
            temp //= 10
    return False

def find_closest(dest_plus,dest_minus):
    global broken
    while True:
        if not has_num(dest_plus,broken) or not has_num(dest_minus,broken):
            break
        dest_plus += 1
        dest_minus -= 1
    if not has_num(dest_plus,broken):
        return dest_plus
    return dest_minus

def find_digit(num):
    digit = 1
    while num > 10:
        digit += 1
        num //= 10
    return digit

closest = find_closest(destination,destination)

print(min(abs(destination-100), find_digit(closest)+abs(closest-destination)))