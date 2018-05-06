def distributeCandies(candies):
    t = int(len(candies)/2)
    s = len(set(candies))
    if t > s:
        return s
    else:
        return t
    
print(distributeCandies([1,1,2,3]))

