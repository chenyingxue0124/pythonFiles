a,b = int(input()),int(input())
#再帰関数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print gcd(a,b)
