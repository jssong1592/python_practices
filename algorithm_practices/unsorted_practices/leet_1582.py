mat = [[1,0,0],[0,0,1],[1,0,0]]

ans = 0
colSum = [sum(i) for i in list(zip(*mat))]
for i in range(len(mat)):
    if sum(mat[i]) == 1:
        a = mat[i].index(1)
        if colSum[a] == 1:
            ans += 1
print(ans)