def aplusb(a,b):
    if b == 0 :
        return a
    elif a == 0 :
        return b
    else:
        summary = a ^ b
        carry = (a & b) << 1
        return aplusb(summary,carry)
    
if __name__ == "__main__":
    print(aplusb(12,14))