def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res
        
print(singleNumber([2,4,5,2,4,6,5,8,12,6,12]))
    