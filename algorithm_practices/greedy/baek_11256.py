cases = int(input())
for i in range(cases):
    j, n = map(int, input().split(' '))
    boxes = []
    for a in range(n):
        r, c = map(int, input().split(' '))
        boxes.append(r*c)

print(boxes)