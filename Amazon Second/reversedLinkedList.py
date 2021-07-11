def reverse(head):
    pre = None
    current = head
    while current is not None:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre