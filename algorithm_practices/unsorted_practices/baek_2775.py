def cell(k,n):
    if k == 0:
        return n
    if n == 0:
        return 0
    return cell(k-1,n) + cell(k,n-1)

print(cell(3,4))

