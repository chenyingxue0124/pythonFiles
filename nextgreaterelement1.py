def nextGreaterElement(findNums,nums):
    d = {}
    st = []
    ans = []
    
    for x in nums:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)
        
    for x in findNums:
        ans.append(d.get(x,-1))
        
    return ans
        
print(nextGreaterElement([1,4,5],[1,6,7,12,5,8,4]))
        