from collections import deque

n,k = map(int,input().split())
visited = [False] * 100001

dq = deque()
dq.append(n)
visited[n] = True
res = 0

while dq:
    l = len(dq)
    res += 1
    for i in range(l):
        p = dq.popleft()
        if p > 0 and not visited[p-1]:
            dq.append(p-1)
            visited[p-1] = True
        if p < 100000 and not visited[p+1]:
            dq.append(p+1)
            visited[p+1] = True
        if 2*p <= 100000 and not visited[2*p]:
            dq.append(2*p)
            visited[2*p] = True
    # print(dq)
    if k in dq:
        break

print(res)