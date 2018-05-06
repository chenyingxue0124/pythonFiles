def firstUniqChar(s):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    index = [s.index(l) for l in letter if s.count(l) == 1 ]
    if len(index) == 0:
        return -1
    else:
        return min(index)
    
print(firstUniqChar('leetcodelove'))