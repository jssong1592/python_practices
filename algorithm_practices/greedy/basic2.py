N, M = map(int, input().split(' '))
arr = [list(map(int,input().split(' '))) for i in range(N)]

print(max([min(each) for each in arr]))