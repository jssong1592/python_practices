'''
input
2
3 ABC
5 /HTP
output
AAABBBCCC
/////HHHHHTTTTTPPPPP
'''

n = int(input())
for _ in range(n):
    num, string = input().split()
    result = [int(num) * ch for ch in string]
    print(''.join(result))