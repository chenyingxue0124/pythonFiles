def largestDivisibleSubset(nums):
    s = {-1:set()}
    for x in sorted(nums):
        s[x] = max((s[d] for d in s if x % d== 0),key = len)|{x}
    return list(max(s.values(),key =len))
                
print (largestDivisibleSubset([13,1,2,4,6]))