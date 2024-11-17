a = [-1,-2,5,8,-3,7,7,2]
def binaryst(arr,target):
    n = len(arr)
    l = 0 
    r = n-1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return True
        elif target < arr [m]:
            r = m - 1
        else:
            l = m + 1
    return -1
print(binaryst(a,-1))
            
