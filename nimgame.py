class Solution(object):
    def canWinNim(self,n):
        return(bool(n%4))  #只要是不能被4整除就是可以赢
    
a = Solution()

print(a.canWinNim(65))
        