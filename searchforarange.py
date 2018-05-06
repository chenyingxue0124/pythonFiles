def searchRange(nums,target): #better
    if len(nums) == 0:
        return [-1,-1]
    else:
        def search(lo,hi):
            if nums[lo] == target == nums[hi]: #if the whole part of nums is full of target
                return [lo,hi]
            if nums[lo] <= target <= nums[hi]:
                mid = int((lo+hi)/2)
                l,r = search(lo, mid),search(mid + 1 , hi)
                return max(l,r) if -1 in l+r else [l[0],r[1]]
            return [-1,-1] #if target is outside the range
        return search(0,len(nums)-1)
          
print(searchRange([1,2,3,3,3,4],3))