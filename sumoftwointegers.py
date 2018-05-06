def getsum(a,b):
    MAX= 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFF
    while b != 0 :
        a,b = (a ^ b) & mask,((a & b) << 1) & mask
    return a if a <= MAX else ~(a ^ mask)

print(getsum(1,-1))

def getsum(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
    return a

print(getsum(-1,3))