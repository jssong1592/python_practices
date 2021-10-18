import sys

not_heard = set()
not_seen = set()

n, m = map(int,sys.stdin.readline().rstrip().split())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    not_heard.add(name)

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    not_seen.add(name)

not_heard_nor_seen = sorted(list(not_heard.intersection(not_seen)))
print(len(not_heard_nor_seen))
if len(not_heard_nor_seen) > 0:
    for i in range(len(not_heard_nor_seen)):
        print(not_heard_nor_seen[i])
