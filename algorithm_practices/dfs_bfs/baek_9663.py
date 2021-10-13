'''
n-queen
input -> 92
8
'''

n = int(input())

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def dfs(n, current_row, current_candidate, final_result):
    if current_row == n:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(n):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(n, current_row+1, current_candidate, final_result)
            current_candidate.pop()

def n_queen(n):
    final_result = []
    dfs(n, 0, [], final_result)
    return final_result

print(len(n_queen(n)))
