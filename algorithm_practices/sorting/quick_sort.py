arr = [7,5,9,0,3,1,6,2,4,8]

# use recursion

def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right],arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quickSort(arr,start,right-1)
    quickSort(arr,right+1,end)
    

quickSort(arr, 0, len(arr)-1)
print(arr)