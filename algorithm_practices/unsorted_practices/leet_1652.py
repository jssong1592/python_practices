'''
If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0

code[n-1] 다음은 code[0], code[0] 전은 code[n-1]
'''

'''
code = [5,7,1,4]
k = 3
Output = [12,10,16,13]
'''

from typing import KeysView


code = [5,7,1,4]
k = 3

code1 = code * 2

def solution(code,k):
    if k == 0:
        return list(0 for i in code)
    elif k > 0:
        return list(sum(code1[i+1:i+1+k]) for i in range(len(code)))
    else:
        return list(sum(code1[i+len(code)+k:i+len(code)]) for i in range(len(code)))


print(solution([5,7,1,4],3))