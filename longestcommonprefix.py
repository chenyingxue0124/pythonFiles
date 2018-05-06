def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) < 1:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else: 
        end, minl = -1, min([len(s) for s in strs])
        if minl== 0:
            return ''
        while end < minl-1:
            end+=1
            s=''
            for i in range(len(strs)):
                s+=strs[i][end]
            if s!=len(strs)*strs[0][end]:
                if end==0:
                    return ''
                else:
                    return strs[0][:end]
        return strs[0][:end+1]

if __name__=='__main__':
    strs = ["ab","ab","abx" ,"abc"]
    print (longestCommonPrefix(strs))    
