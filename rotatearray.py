def rotate(nums,k):
    if nums == []:
        return([])
    elif k == 0:
        return(nums)
    else:
        n = len(nums)
        k = k % n
        nums[:]= nums[n-k:] + nums[:n-k]
        return(nums[:])
    
print(rotate([1,2,3,4,5,6,7],3))