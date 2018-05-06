def searchRange(nums,target):
    def search(n):
        lo,hi = 0,len(nums)
        while lo < hi:
            mid = int((lo + hi)/2)
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
    lo = search(target)
    return [lo,search(target+1)-1] if target in nums[lo:lo+1] else [-1,-1]
    
print(searchRange([1,2,3,3,3,3,4,5,6],3))