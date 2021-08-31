N = int(input())
i = 2
j = 1
while i <= N:
    if N % i == 0:
        print(i)
        N /= i
    else:
        j += 2
        i = j