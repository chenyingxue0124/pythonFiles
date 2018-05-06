def deleteDuplicates(self, head):
    if head == None: 
        return head

    node = head

    while node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next

    return head    