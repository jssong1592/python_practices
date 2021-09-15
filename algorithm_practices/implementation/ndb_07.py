'''
input => LUCKY
123402

input => READY
7755
'''

n = input()

a = n[:len(n)//2]
b = n[len(n)//2:]


if sum(map(int,a)) == sum(map(int,b)):
    print("LUCKY")
else:
    print("READY")