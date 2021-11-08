# 마지막 R << min(G,B)
# 마지막 G << min(R,B)
# 마지막 B << min(R,G)

'''
input
3
26 40 83
49 60 57
13 89 99
'''

n = int(input())
cost = [[]]
for i in range(n):
    cost.append(list(map(int,input().split())))

total_cost = [cost[1]]
for i in range(2,n+1):
    total_cost.append([cost[i][0]+min(total_cost[-1][1],total_cost[-1][2]),cost[i][1]+min(total_cost[-1][0],total_cost[-1][2]),cost[i][2]+min(total_cost[-1][0],total_cost[-1][1])])

print(min(total_cost[-1]))