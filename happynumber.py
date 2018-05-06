def isHappy(n):
    mem = set() #prevent same digits
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)]) #calculate the sum of the squres of its digits
        if n in mem: # means it loops endlessly in a cycle
            return False
        else:
            mem.add(n) #add new n
    else:
        return True

print(isHappy(1))
    
    
    
    
    