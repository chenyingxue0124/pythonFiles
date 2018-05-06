def reverse(x):
    if x > 0: #用切片来进行反转，但是需要注意切片只能用在str而且要注意负数的情况
        num = (int(str(x)[::-1]))
    else:
        num =int(str(x*-1)[::-1])*-1
    if abs(num) > 2 **31 -1:
        return 0
    else:
        return num
    
print(reverse(123))