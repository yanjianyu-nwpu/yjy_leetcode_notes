a = [1,3,8,20,20,20,29,120]

def find(target,nums):
    print("FIND ",target,nums)
    
    st = 0
    ind = len(nums)-1
    if nums[st] >= target:
        return 0
    if target > nums[ind]:
        return -1
    
    while st < ind:
        
        mid = int((st + ind)/2)
        print(st,ind,mid,nums[mid])
        if target < nums[mid]:
            ind = mid
        else:
            st = mid + 1 
    return ind
    
print(find(1,a))
print(find(2,a))
print(find(3,a))
print(find(8,a))
print(find(9,a))
print(find(20,a))
print(find(28,a))
print(find(29,a))
print(find(120,a))
print(find(120,a))