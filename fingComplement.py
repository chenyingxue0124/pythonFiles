def findComplement(num):
    mask = ~0
    while((mask & num)!= 0):
        mask <<= 1
    return ((~mask) & (~num))
    
    

print(findComplement(16))