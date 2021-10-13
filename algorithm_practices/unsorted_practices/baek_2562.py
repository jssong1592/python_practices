'''
input -> 8 
3
29
38
12
57
74
40
85
61
'''

lst = []
for _ in range(9):
    lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)