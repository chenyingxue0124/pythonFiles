import math

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b 
        n = n+1
    return 'done'


def twoSum(nums, target):
    aDict={}
    for i,num in enumerate(nums):
        if target-num in aDict:
            print(aDict[target-num],i)
        else:
            aDict.update({num:i})
        
    
def reverse(x):
    isNeg=False
    if x<0:
        x=-x
        isNeg=True
    s=str(x)
    t=0
    i=0
    while i<len(s):
        t+=int(s[len(s)-i-1])*int('1'+'0'*(len(s)-i-1))
        i+=1
    if isNeg:
        if -t<-2147483647:
            return 0
        return -t
    else:
        if t>2147483647:
            return 0
        return t
    
def pseudoPower(pow):
    return int('1'+'0'*pow)
    

if __name__=='__main__':
    testCase=[[3,2,4],[1,5,6,5], [1,2,2,4]]
    target=[6,10,5]
    testCase2=[-123,47352,-1, 0, 1534236469, 2147483647]
    for i,test in enumerate(testCase2):
        print(reverse(test))

    


    

