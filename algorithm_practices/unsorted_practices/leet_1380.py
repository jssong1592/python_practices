## Given m * n matrix of distinct numbers, return all lucky numbers
## lucky number = minimum in the row AND maximum in the column

matrix = [[3,7,8],[9,11,13],[15,16,17]] ## input example

m = len(matrix)
n = len(matrix[0])

print(m)
print(n)

res = []
for i in range(m):
    row = matrix[i]
    for j in range(n):
        col = [num[j] for a,num in enumerate(matrix)]
        if min(row) == max(col):
            res.append(min(row))

print(res)


## zip을 활용한 one-liner solution
## unpacking operator(*)-->리스트 언패킹, intersection operator(&)--> set 자료형의 교집합연산자, zip 함수 활용법 정리하기
'''
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})
'''




