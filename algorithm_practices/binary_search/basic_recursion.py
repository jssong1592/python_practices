def binary_search(arr, target, start, end):
    if start > end:
        return None
    middle = (start+end)//2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search(arr, target, middle+1, end)
    else:
        return binary_search(arr, target, start, middle-1)

n, target = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))

print(binary_search(arr, target, 0, len(arr)-1))

