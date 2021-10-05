import sys
from collections import Counter

word = sys.stdin.readline().rstrip().upper()

c = Counter(word)
lst = c.most_common()

if len(lst) == 1:
    print(lst[0][0])
else:
    if lst[0][1] == lst[1][1]:
        print('?')
    else:
        print(lst[0][0])
