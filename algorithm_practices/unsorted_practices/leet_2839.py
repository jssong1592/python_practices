n = int(input())
a,b = n//5, n%5
while b % 3 != 0:
    if a == 0:
        break
    a -= 1
    b += 5 
if b % 3 == 0:
    print(int(a+(b/3)))
else:
    print(-1)