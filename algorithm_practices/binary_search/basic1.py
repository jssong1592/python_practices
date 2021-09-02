import sys

n = int(sys.stdin.readline().rstrip())
inv = sys.stdin.readline().rstrip().split(' ')
inv = sorted(list(map(int, inv)))
m = int(sys.stdin.readline().rstrip())
check = sys.stdin.readline().rstrip().split(' ')
check = list(map(int, check))

def binary_search(arr, target, start, end):
    if start > end:
        return "no"
    middle = (start+end)//2
    if arr[middle] == target:
        return "yes"
    elif arr[middle] < target:
        return binary_search(arr, target, middle+1, end)
    else:
        return binary_search(arr, target, start, middle-1)


for i in range(m):
    print(binary_search(inv, check[i], 0, len(inv)-1), end=' ')