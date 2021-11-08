import sys

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

def is_compressable(graph):
    total = sum([sum(graph[i]) for i in range(len(graph))])
    if total == 0 or total == len(graph) ** 2:
        return True
    return False

def compress(graph):
    if is_compressable(graph):
        return str(graph[0][0])
    elif not is_compressable(graph):
        if len(graph) == 2:
            return '(' + str(graph[0][0]) + str(graph[0][1]) + str(graph[1][0]) + str(graph[1][1]) + ')'
        return ('(' + compress([[graph[i][j] for j in range(len(graph)//2)] for i in range(len(graph)//2)]) + 
        compress([[graph[i][j] for j in range(len(graph)//2,len(graph))] for i in range(len(graph)//2)]) + 
        compress([[graph[i][j] for j in range(len(graph)//2)] for i in range(len(graph)//2,len(graph))]) + 
        compress([[graph[i][j] for j in range(len(graph)//2,len(graph))] for i in range(len(graph)//2,len(graph))]) + ')')

print(compress(graph))