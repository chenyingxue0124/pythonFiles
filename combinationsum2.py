def combinationSum2(candidates,target):
    def dfs(nums,target,index,path,res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue #continue是跳出本次循环，break是跳出整个循环，跳出当前循环的剩余语句，继续进行下一轮循环，不执行下一行dfs了
            dfs(nums,target-nums[i],i+1,path+[nums[i]],res)
    res = []
    candidates.sort()
    dfs(candidates,target,0,[],res)
    return res

print(combinationSum2([10,1,2,7,6,1,5],8))