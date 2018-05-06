#import math
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
        
    

if __name__=='__main__':
    testCase=[[3,2,4],[1,5,6,5], [1,2,2,4]]
    target=[6,10,5]
    for i,test in enumerate(testCase):
        twoSum(test, target[i])

    


    

