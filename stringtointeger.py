
def myAtoi(str):
        if len(str) == 0:
                return(0)
        ans = 0 #进行各种标记
        number_started = False #进行开头的标记
        sign = 1
        signflag = False
        for i in str: #一开始是空格就跳过，中间是空格就终止
                if i == " ":
                        if number_started == False:
                                continue
                        else:
                                break
                elif (i == "+" or i == "-") and number_started ==False and signflag == False: #符号有无的情况,if character is a sign and the number is not yet started then save the sign 
                        if i == "-":
                                sign = -1
                        else:
                                sign = 1
                        signflag = True
                        number_started = True
                elif ord(i) >= 48 and ord(i) <= 57: #0-9对应的ascii值是这个区间
                        number_started = True
                        ans = (ans * 10) + (ord(i) - ord("0"))
                        
                else:
                        break
                
        if ans >= 2**31: #边界的情况
                ans = 2**31
                if sign == 1:
                        return ans -1
                else:
                        return sign * ans
        return sign * ans
                        
print(myAtoi("+1"))