from collections import Counter

num = 1
for _ in range(3):
    num *= int(input())

c = Counter(str(num))

for i in range(10):
    print(c[str(i)])