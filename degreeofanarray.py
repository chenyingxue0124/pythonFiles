from collections import Counter
from collections import defaultdict

def findShortestSubArray(nums):
    nums_map = defaultdict(list) #有默认值的字典
    deg = 0
    min_len = float('inf')#正无穷
    for index, num in enumerate(nums): #将index 和 num进行循环
        nums_map[num].append(index) #key是num,value是index
        deg  = max(deg, len(nums_map[num]))
    for num, indices in nums_map.items():
        if len(indices) == deg:
            min_len = min(min_len, indices[-1] - indices[0] + 1)
    return min_len

print(findShortestSubArray([1,2,2,3,1,4,2]))
    
    
    