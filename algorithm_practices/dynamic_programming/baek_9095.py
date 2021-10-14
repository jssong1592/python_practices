'''
input
3
4
7
10
output
7
44
274
'''

combi = [1,2,4]

n = int(input())
for i in range(n):
    num = int(input())
    length = len(combi)
    if num > length:
        for j in range(length,num):
            combi.append(combi[-1]+combi[-2]+combi[-3])
    print(combi[num-1])
