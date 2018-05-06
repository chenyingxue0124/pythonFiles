#def climbingStairs(n):
    #if n == 1:
        #return 1
    #res = [0 for i in range(n)]
    #res[0], res[1] = 1,2
    #for i in range(1,n):
        #res[i] = res[i-1] + res[i-2]
    #return res[-1]

def climbingStairs(n):
    if n == 1:
        return 1
    a,b = 1,2
    for i in range(2,n):
        tmp = b
        b = a+b
        a = tmp
    return b
    
    
    
    
print(climbingStairs(35))
