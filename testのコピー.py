from functools import reduce
def add(x,y):
    return x+y

if __name__=='__main__':
    print(reduce(add,[1,3,5,7,9]))
    
    
    
    
