def findwords(words):
    a = set("qwertyuiop")
    b = set("asdfghjkl")
    c = set("zxcvbnm")
    ans = []
    for word in words:
        t = set(word.lower())
        if t.issubset(a) or t.issubset(b) or t.issubset(c):
            ans.append(word)
    return ans
    
print(findwords(["Hello", "Alaska", "Dad", "Peace"]))
    
#a = set("qwertyuiop")
    #b = set("asdfghjkl")
    #c = set("zxcvbnm")
    #ans = []
    #for word in words:
        #t = set(word.lower())
        #if a & t == t:
            #ans.append(word)
        #elif b & t == t:
            #ans.append(word)
        #elif c & t == t:
            #ans.append(word)
    #return ans    