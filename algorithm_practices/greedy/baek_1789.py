s = int(input())
n = 0
while True:
    n += 1
    if s < ((1+n)*n)//2:
        break
    
print(n-1)