def lengthOfLongestSubstring(s):
    start = longestsub = 0 # return the number of substring
    usedchar = {} # memory the used char
    for i in range(len(s)): #use the index 不用range的话输出的就是字符了
        if s[i] in usedchar and start <= usedchar[s[i]]:
            start = usedchar[s[i]] + 1
        else:
            longestsub = max(longestsub,i-start + 1) #if there're some substrings,choose the longest one
            
        usedchar[s[i]] = i #add i in dictionary
    
    return longestsub
    
print(lengthOfLongestSubstring("pwwkew"))