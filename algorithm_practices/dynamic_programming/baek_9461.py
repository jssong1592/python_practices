# 1 1 1 2 2 3
# 4 5 7 9 12 16

# n = n-1 + n-5


dp = [0,1,1,1,2,2]

for i in range(6,101):
    dp.append(dp[i-1]+dp[i-5])

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
