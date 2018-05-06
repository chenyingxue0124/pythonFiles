class ListNode(object): #定义链表
    def __init__(self,x):
        self.val = x
        self.next = None  #把必须绑定的属性强制填写进去

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        addends = l1,l2 #先把两个链表合并
        dummy = end = ListNode(0)  #建立两个空的链表
        carry = 0 #用于进位
        while addends or carry: #当都不是零的时候
            carry += sum(a.val for a in addends) #选取第一位进行相加
            addends = [a.next for a in addends if a.next] #开始指到下一位
            end.next = end = ListNode(carry % 10) #留在位子上的
            carry /= 10 #进位
        return dummy.next
        
        
                 
    if __name__=='__main__':
        print(addTwoNumbers([2,4,3],[5,6,4]))