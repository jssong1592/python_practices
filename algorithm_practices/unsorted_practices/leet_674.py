nums = [1,3,5,4,7]

inc = max_inc = 1
for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
        inc += 1
    else:
        inc = 1
    if inc > max_inc:
        max_inc = inc
                
print(max_inc)