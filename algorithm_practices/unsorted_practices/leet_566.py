'''
m*n 행렬을 r*c행렬로 변환, 행렬 변환이 불가능하면 원래 mat return
'''

mat = [[1,2],[3,4]]
r = 1
c = 4

# output = [[1,2,3,4]]

from itertools import chain

def reshape(mat,r,c):
    elements = list(chain(*mat))
    if r*c == len(elements):
        output = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(elements[i*c+j])
            output.append(row)
        return output
    return mat