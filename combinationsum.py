def combinationSum(candidates,target):
    res = []
    dfs(candidates,target,0,[],res)
    return res

def dfs(nums,target,index,path,res):
    if target < 0: #先判断，不然很容易进入死循环，不断的调用自己，所以递归一般都先判断
        return
    if target == 0:#在编写递归调用的函数的时候，一定要把简单情景的判断写在最前面，以保证函数调用在检查到简单情境的时候能够及时的终止递归。否则可能死循环
        res.append(path)
        return
    for i in range(index,len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

print(combinationSum([2,3,5,6],7))