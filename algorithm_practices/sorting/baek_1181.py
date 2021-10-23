'''
input
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

output
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''
from collections import defaultdict

n = int(input())
lst = defaultdict(set)
max_length = 0
for _ in range(n):
    word = input()
    if len(word) > max_length:
        max_length = len(word)
    lst[len(word)].add(word)
word_lst = [[] for i in range(max_length+1)]
for key in lst:
    for word in lst[key]:
        word_lst[key].append(word)
    word_lst[key].sort()

for i in range(len(word_lst)):
    if len(word_lst[i]) > 0:
        for j in range(len(word_lst[i])):
            print(word_lst[i][j])
