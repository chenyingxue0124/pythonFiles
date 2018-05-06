class ListNode(object):
    def __init__ (self,x, n=None):
        self.val = x
        self.next = n
    
    def __str__(self):
        return str(self.val)
    
    
def mergeTwoLists(l1,l2):
    dummy = ListNode(0)
    tmp = dummy
    while l1 != None and l2 !=None:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    if l1 != None:
        tmp.next = l1
    else:
        tmp.next = l2
    return dummy.next

def toLinkedList(x):
    tmp=ListNode(x[-1])
    for i in range(1,len(x)):
        tmp=ListNode(x[len(x)-i-1],tmp)
    return tmp

def printListNode(ln):
    print(ln.val)
    while(ln.next!=None):
        ln=ln.next
        print(ln.val)

if __name__=='__main__':
    l1 = toLinkedList([2,4,5,1,6])
    l2 = [5,5,6,1,2]
    
    result=mergeTwoLists(l1, l2)
    
    printListNode(result)

