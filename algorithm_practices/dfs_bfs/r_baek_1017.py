'''
input
6
1 4 7 10 11 12
output
4 10
'''

import sys

prime_list = [True for i in range(2000)]
def prime():
    prime_list[1] = False
    for i in range(2,int(1999**0.5)+1):
        if prime_list[i]:
            for j in range(i*2,2000,i):
                prime_list[j] = False

prime()


n = int(input())
lst = sys.stdin.readline().rstrip().split()

lst1 = []
lst2 = []
for num in lst:
    if int(num) % 2 == int(lst[0]) % 2:
        lst1.append(int(num))
    else:
        lst2.append(int(num))

graph = [[] for i in range(len(lst1)+1)]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if prime_list[lst1[i]+lst2[j]]:
            graph[i+1].append(j+1)

def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    for i in graph[start]:
        if used[i] == 0 or dfs(used[i]):
            used[i] = start
            return 1
    return 0

result = []

for i in graph[1]:
    used = [0 for _ in range(len(lst2)+1)]
    used[i] = 1
    cnt = 1
    for j in range(1,len(lst1)+1):
        visit = [0 for _ in range(len(lst1)+1)]
        visit[1] = 1
        cnt += dfs(j)
    if cnt == n // 2:
        result.append(lst2[i-1])
if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i,end=' ')