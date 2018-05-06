def deleteDuplicates(head):
    if head == None: #判断空链表的情况
        return None
    d = ListNode(0) #建立一个空链表
    d.next = head #d的下一个指向head的表头
    tmp = d #复制一个到tmp
    while tmp and tmp.next and tmp.next.next:
        if tmp.next.val == tmp.next.next.val:
            de = tmp.next.next
            while de.next and de.next.val == tmp.next.val:
                de = de.next
            tmp.next = de.next
        if tmp.next and tmp.next.next and tmp.next.val != tmp.next.next.val:
            tmp = tmp.next
    return d.next
            
            
            
            
        