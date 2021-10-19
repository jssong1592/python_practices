'''
input -> 75
6
10
20
15
25
10
20
'''

n = int(input())

step = []

for _ in range(n):
    step.append(int(input()))

dp = [0] * n
dp[0] = step[0]
if n >= 2:
    dp[1] = max(step[0] + step[1], step[1])
if n >= 3:
    dp[2] = max(step[0] + step[2], step[1] + step[2])
if n > 3:
    for i in range(3,n):
        dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])

print(dp[-1])