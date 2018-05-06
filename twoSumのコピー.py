def twoSum(nums,target):
    adict = {}
    for i,num in enumerate(nums):
        if target-num in adict:
            return adict[target-num],i
        else:
            adict.update({num:i})
            
print(twoSum([3,3,4,5],6))
 