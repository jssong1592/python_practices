n = int(input())
w_list = sorted(list(map(int,input().split(' '))))
team = [w_list[i]+w_list[-1*(i+1)] for i in range(n)]

print(min(team))