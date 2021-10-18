import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
poke_dex = {}
for i in range(1,n+1):
    pokemon = sys.stdin.readline().rstrip()
    poke_dex[i] = pokemon
    poke_dex[pokemon] = i

for _ in range(m):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isnumeric():
        print(poke_dex[int(quiz)])
    else:
        print(poke_dex[quiz])