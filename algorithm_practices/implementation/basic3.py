col = ['a','b','c','d','e','f','g','h']
row = ['1','2','3','4','5','6','7','8']

result = 0

data = input()

x = col.index(data[0])
y = row.index(data[1])

## ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ....
if y - 2 in range(8):
    if x - 1 in range(8):
        result += 1
    if x + 1 in range(8):
        result += 1
if y + 2 in range(8):
    if x - 1 in range(8):
        result += 1
    if x + 1 in range(8):
        result += 1
if y - 1 in range(8):
    if x - 2 in range(8):
        result += 1
    if x + 2 in range(8):
        result += 1
if y + 1 in range(8):
    if x - 2 in range(8):
        result += 1
    if x + 2 in range(8):
        result += 1

print(result)
