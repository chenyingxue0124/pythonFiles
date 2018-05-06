class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x > 0: 
            num = (int(str(x)[::-1]))
        elif x == 0:
                return True
        else:
            return False
        if abs(num) > 2 **31 -1:
            return False
        else:
            if x == num:
                return True
            else:
                return False


if __name__ == "__main__":
    n = int(input("请输入一个数字："))
    a = Solution()
    print(a.isPalindrome(n))