class Solution(object):
    def romanToInt(self,s):
        Sum = 0
        convert = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1} #使用字典
        for i in range(len(s)-1): #比较到倒数第二个数
            if convert[s[i]] < convert[s[i+1]]:
                Sum = Sum - convert[s[i]]
            else:
                Sum = Sum + convert[s[i]]
        return Sum + convert[s[-1]]

a = Solution()
print(a.romanToInt("MCDLXXVI"))