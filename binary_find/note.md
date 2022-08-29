# binary search

# 二分查找



## 0 introduction

    二分查找，不用多说 ，事件复杂度logn；本文主要论述其在做的时候的具体实现，均python实现

## 1 simple 找到指定值

```
a = [1,3,8,20,29,120]

def find(target,nums):
    print("FIND ",target,nums)
    st = 0
    ind = len(nums)-1
    while st <= ind:
        mid = int((st + ind)/2)
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            st = mid + 1
        else:
            ind = mid -1 
    return -1
    
print(find(1,a))
print(find(2,a))
print(find(3,a))
print(find(8,a))
print(find(9,a))
print(find(20,a))
print(find(29,a))
print(find(120,a))
```

主要问题 在四个地方

- while 判断条件

- st 对比mid 的移动条件

- ind 对比 mid 的移动条件

- 改mid 的判断条件，是调整 st 还是 ind

感觉最危险的就是 while 判断条件   容易造成死循环 这里还是要等于 = ，但是后面st 一定要 mid+1，ind 一定要 mid-1 因为不然就会出不来



## 2 判断大于等于某个值的最小坐标

```
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
        if target <= nums[mid]:
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
```

这里思路就是不必要和 查找一样，所有的          都需要比较

- 先判断是不是在区间内

- 不需要对比所有元素，把while 上的 = 去掉

- 然后判断条件，因为找第一个大于的，所有 <=  ,且 ind = mid 因为返回的是ind ，要稳

死循环的关键在于         

    没有+1 的那一个反复执行  就是 mid = ind 然后ind 和mid 反复执行，但是因为 （ind+st） 会偏向st 所以不会成立

## 3 判断大于某个值的最小坐标

```
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
```


